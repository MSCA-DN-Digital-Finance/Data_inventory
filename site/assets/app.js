'use strict';
(() => {
  const data = JSON.parse(document.getElementById('inventory-data').textContent);
  const {config} = data;
  const people=new Map((data.people||[]).map(p=>[p.number,p]));
  const irpLabel=number=>{const p=people.get(number);return p?`IRP ${number} · ${p.candidate?.name||p.short_title}`:`IRP ${number}`;};
  const entries = [...data.datasets.map(r => ({...r, kind:'dataset', name:r.dataset_name})), ...data.sources.map(r => ({...r, kind:'source'}))];
  const labels = {public:'Public access',request:'Request access',institutional:'Institutional licence',restricted:'Restricted',unknown:'Not documented'};
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const split = value => (value || '').split(';').map(x => x.trim()).filter(Boolean);
  const safeURL = value => {try {const u=new URL(value);return ['https:','http:'].includes(u.protocol)?u.href:'';} catch {return '';}};
  const badge = r => `<span class="badge ${esc(r.access_category)}">${labels[r.access_category] || labels.unknown}</span>`;
  const unknown = '<span class="unknown-value">Not yet documented</span>';
  const fact = (name,value) => `<div><dt>${esc(name)}</dt><dd>${value ? esc(value) : unknown}</dd></div>`;
  const entryURL = r => `#${r.kind}/${r.id}`;
  const link = (url,text,css='text-link') => safeURL(url) ? `<a class="${css}" href="${esc(safeURL(url))}" target="_blank" rel="noopener noreferrer">${esc(text)} ↗</a>` : '';
  const detail = document.getElementById('detail');
  let returnFocus;
  function showDetail(r) {
    if (!detail) return;
    returnFocus = document.activeElement;
    const sourceIds = split(r.source_ids);
    const related = r.kind === 'dataset' ? entries.filter(x => x.kind === 'source' && sourceIds.includes(x.id)) : entries.filter(x => x.kind === 'dataset' && split(x.source_ids).includes(r.id));
    document.getElementById('detail-content').innerHTML = `<header class="detail-header"><div class="eyebrow muted">${r.kind === 'dataset' ? 'RESEARCH DATASET' : 'DATA SOURCE'} · ${esc(r.region || 'Geography not documented')}</div><h2 id="detail-title">${esc(r.name)}</h2><p>${esc(r.short_description)}</p><div class="tags">${split(r.subjects).map(x=>`<span class="tag">${esc(x)}</span>`).join('')}</div></header><div class="detail-body"><section class="access-panel"><h3>Access & conditions</h3>${badge(r)}<p>${esc(r.access_notes || r.availability || r.access)}</p>${link(r.link,r.kind === 'source' ? 'Visit provider' : 'Open dataset location','button small')}${r.kind==='dataset' && !r.link ? '<p>No direct dataset location is documented. Check the linked sources or ask the contributing IRP.</p>' : ''}</section><dl class="detail-grid">${fact('Collection / delivery',r.collection || r.availability)}${fact('File formats',split(r.formats).join(', '))}${fact('Observation / update frequency',r.frequency)}${fact('Publication lag',r.publication_lag)}${fact('Available coverage',r.kind==='dataset' ? [r.first_date,r.last_date].filter(Boolean).join(' → ') : r.history)}${fact('History & version notes',r.history_notes)}${fact('Data quality & limitations',r.quality_notes || r.clean)}${fact('Revisions & vintages',r.revision_policy)}${fact('Licence & reuse',r.license_notes)}${fact('Unit of observation',r.unit_of_observation)}${fact('Contributing IRP',split(r.IRP).map(irpLabel).join('; '))}${fact('Research project',r.irp_titles)}${fact('Doctoral candidate(s)',r.researcher_names)}${fact('Last metadata review',r.last_reviewed)}</dl>${related.length?`<section class="related"><h3>${r.kind==='dataset'?'Related data sources':'Datasets in this inventory'}</h3>${related.map(x=>`<button type="button" data-open="${esc(entryURL(x))}">${esc(x.name)} ↗</button>`).join('')}</section>`:''}<div class="detail-links">${split(r.IRP).filter(n=>/^\d+$/.test(n)).map(n=>`<a class="text-link" href="/irps/irp-${n}.html">IRP ${n} profile ↗</a>`).join('')}${link(r.documentation_url,'Read documentation')}<a class="text-link" href="contribute.html?kind=${r.kind}&id=${encodeURIComponent(r.id)}">Suggest an update ↗</a><button class="text-button" id="copy-link">Copy entry link</button></div><p class="detail-provenance"><strong>About this record.</strong> ${esc(r.provenance || 'Contributor-reported metadata; independent verification is not documented.')} Missing fields are unknown, and do not imply that restrictions or quality problems are absent. Public availability does not by itself grant redistribution rights.</p></div>`;
    if (!detail.open) detail.showModal();
    document.body.classList.add('no-scroll');
    document.getElementById('copy-link').addEventListener('click',async event=>{
      try {await navigator.clipboard.writeText(location.href); event.target.textContent='Link copied';}
      catch {event.target.textContent='Copy the URL from your address bar';}
    });
  }
  function route() {
    const match = location.hash.match(/^#(dataset|source)\/([a-z0-9-]+)$/);
    const r = match && entries.find(x=>x.kind===match[1] && x.id===match[2]);
    if(r) showDetail(r); else if(detail?.open) detail.close();
  }
  if(detail) {
    document.getElementById('close-detail').addEventListener('click',()=>detail.close());
    detail.addEventListener('click',event=>{if(event.target===detail){const box=detail.getBoundingClientRect();if(event.clientX<box.left||event.clientX>box.right||event.clientY<box.top||event.clientY>box.bottom) detail.close();}});
    detail.addEventListener('close',()=>{document.body.classList.remove('no-scroll');if(/^#(dataset|source)\//.test(location.hash)) history.replaceState(null,'',location.pathname+location.search+'#catalogue');if(returnFocus?.isConnected) returnFocus.focus();});
    document.addEventListener('click',event=>{const button=event.target.closest('[data-open]');if(button){if(location.hash===button.dataset.open) route();else location.hash=button.dataset.open;}});
    addEventListener('hashchange',route);
  }
  if(document.getElementById('results')) {
    document.getElementById('dataset-total').textContent=data.datasets.length;
    document.getElementById('source-total').textContent=data.sources.length;
    const kind=document.body.dataset.catalogueKind||'source';
    const catalogueEntries=entries.filter(r=>r.kind===kind);
    const params=new URLSearchParams(location.search);
    // Preserve older shared dataset filter links after splitting the catalogues.
    if(kind==='source'&&params.get('type')==='dataset'){
      params.delete('type');
      location.replace('datasets.html'+(params.size?'?'+params.toString():'')+location.hash);
      return;
    }
    const fields = ['access','subject','region','irp','format'];
    for(const [field,key] of [['subject','subjects'],['region','region'],['irp','IRP'],['format','formats']]) {
      const select=document.getElementById(`${field}-filter`);
      const values=[...new Set(catalogueEntries.flatMap(r=>split(r[key])))].sort((a,b)=>a.localeCompare(b,undefined,{numeric:true}));
      for(const value of values){const option=document.createElement('option');option.value=value;option.textContent=field==='irp'?irpLabel(value):value;select.append(option);}
    }
    const cloud=document.getElementById('subject-cloud');
    const subjectCounts=new Map();
    catalogueEntries.forEach(r=>new Set(split(r.subjects)).forEach(subject=>subjectCounts.set(subject,(subjectCounts.get(subject)||0)+1)));
    const subjects=[...subjectCounts].sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0]));
    const maxCount=Math.max(1,...subjectCounts.values());
    cloud.innerHTML=`<button class="subject-chip subject-all" data-subject="" aria-pressed="true">All subjects</button>`+subjects.map(([subject,count])=>`<button class="subject-chip" data-subject="${esc(subject)}" aria-pressed="false" style="--subject-size:${(14+12*Math.sqrt(count/maxCount)).toFixed(1)}px"><span>${esc(subject)}</span><span class="subject-count" aria-label="${count} ${kind==='dataset'?(count===1?'dataset':'datasets'):(count===1?'data source':'data sources')}">${count}</span></button>`).join('');
    cloud.addEventListener('click',event=>{
      const button=event.target.closest('[data-subject]');
      if(!button)return;
      const selected=document.getElementById('subject-filter');
      const subject=selected.value===button.dataset.subject?'':button.dataset.subject;
      reset();selected.value=subject;render();
      document.getElementById('inventory-filters').classList.remove('mobile-open');
      document.getElementById('toggle-filters').setAttribute('aria-expanded','false');
      document.getElementById('catalogue-results').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth',block:'start'});
    });
    for(const field of fields){const el=document.getElementById(`${field}-filter`);if(params.has(field))el.value=params.get(field);el.addEventListener('change',()=>render());}
    const search=document.getElementById('search');search.value=params.get('q')||'';search.addEventListener('input',()=>render());
    const sort=document.getElementById('sort');sort.value=params.get('sort')==='reviewed'?'reviewed':'name';sort.addEventListener('change',()=>render());
    document.getElementById('toggle-filters').addEventListener('click',event=>{
      const open=document.getElementById('inventory-filters').classList.toggle('mobile-open');
      event.currentTarget.setAttribute('aria-expanded',String(open));
    });
    const reset=()=>{search.value='';fields.forEach(f=>document.getElementById(`${f}-filter`).value='');sort.value='name';render();};
    document.getElementById('reset').addEventListener('click',reset);document.getElementById('empty-reset').addEventListener('click',reset);
    document.addEventListener('keydown',event=>{if(event.key==='/'&&!['INPUT','TEXTAREA','SELECT'].includes(event.target.tagName)&&!detail.open){event.preventDefault();search.focus();}});
    function render() {
      const query=search.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
      const filters=Object.fromEntries(fields.map(f=>[f,document.getElementById(`${f}-filter`).value]));
      const found=catalogueEntries.filter(r=>query.every(q=>Object.values(r).join(' ').toLowerCase().includes(q))&&(!filters.access||r.access_category===filters.access)&&(!filters.subject||split(r.subjects).includes(filters.subject))&&(!filters.region||split(r.region).includes(filters.region))&&(!filters.irp||split(r.IRP).includes(filters.irp))&&(!filters.format||split(r.formats).includes(filters.format))).sort((a,b)=>sort.value==='reviewed' ? (b.last_reviewed||'').localeCompare(a.last_reviewed||'')||a.name.localeCompare(b.name):a.name.localeCompare(b.name));
      cloud.querySelectorAll('[data-subject]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.subject===filters.subject)));
      const viewTitle=kind==='dataset'?'Datasets':'Data sources';
      document.getElementById('list-title').textContent=filters.subject?`${viewTitle}: ${filters.subject}`:kind==='source'?'All data sources':'All datasets';
      const download=document.getElementById('download-csv');
      const downloadDatasets=kind==='dataset';
      download.href=downloadDatasets?'data/datasets.csv':'data/data-sources.csv';
      download.textContent=downloadDatasets?'Download datasets CSV ↓':'Download sources CSV ↓';
      document.getElementById('result-count').textContent=`${found.length} ${kind==='source'?(found.length===1?'source':'sources'):kind==='dataset'?(found.length===1?'dataset':'datasets'):(found.length===1?'entry':'entries')}`;
      document.getElementById('empty').hidden=found.length>0;
      document.getElementById('results').innerHTML=found.map(r=>`<article class="entry"><div><div class="entry-top"><span class="entry-type">${r.kind==='dataset'?'RESEARCH DATASET':'DATA SOURCE'}</span><span class="entry-type">${esc(r.region || 'Region not documented')}</span></div><h3><button class="entry-title" data-open="${esc(entryURL(r))}">${esc(r.name)}</button></h3><p>${esc(r.short_description)}</p><div class="tags">${split(r.subjects).map(x=>`<span class="tag">${esc(x)}</span>`).join('')}</div></div><div class="entry-aside">${badge(r)}<div class="entry-fact">${r.kind==='dataset'?`<strong>${esc(r.frequency||'Frequency unknown')}</strong><br>${esc(r.first_date||'?')} → ${esc(r.last_date||'?')}`:`<strong>${esc(r.collection||'Collection not documented')}</strong>`}</div>${r.publication_lag?`<span class="entry-fact">Lag: ${esc(r.publication_lag)}</span>`:''}<button data-open="${esc(entryURL(r))}" aria-label="${esc('View details for '+r.name)}">View research notes ↗</button></div></article>`).join('');
      const next=new URLSearchParams();if(search.value)next.set('q',search.value);for(const f of fields)if(filters[f])next.set(f,filters[f]);if(sort.value!=='name')next.set('sort',sort.value);
      history.replaceState(null,'',location.pathname+(next.size?'?'+next.toString():'')+location.hash);
    }
    render();route();
  }
  const form=document.getElementById('contribution-form');
  if(form){
    const status=document.getElementById('form-status');
    const params=new URLSearchParams(location.search);
    const kindSelect=form.elements.kind;
    const irpChoices=document.createElement('datalist');irpChoices.id='irp-choices';
    for(const p of people.values()){const option=document.createElement('option');option.value=p.number;option.label=irpLabel(p.number);irpChoices.append(option);}
    form.elements.IRP.setAttribute('list','irp-choices');form.append(irpChoices);

    const sourceList=form.elements.source_ids;
    data.sources.forEach(r=>{const option=document.createElement('option');option.value=r.id;option.textContent=r.name;sourceList.append(option);});
    function syncKind(){document.querySelectorAll('[data-for]').forEach(el=>{el.hidden=el.dataset.for!==kindSelect.value;el.querySelectorAll('input,select,textarea').forEach(input=>input.disabled=el.hidden);});}
    kindSelect.addEventListener('change',syncKind);
    const existing=entries.find(r=>r.id===params.get('id')&&r.kind===params.get('kind'));
    if(existing){kindSelect.value=existing.kind;form.elements.action.value='update';form.elements.id.value=existing.id;for(const el of form.elements){if(!el.name||['kind','action','id'].includes(el.name))continue;const value=existing[el.name];if(value!==undefined){if(el.multiple) [...el.options].forEach(o=>o.selected=split(value).includes(o.value));else el.value=value;}}form.elements.name.value=existing.name;if(existing.kind==='dataset')form.elements.collection.value=existing.availability||'';}
    syncKind();
    let proposal=null;
    function collect(){
      const values=new FormData(form);const record={};
      for(const [key,value] of values){if(['kind','action'].includes(key))continue;if(key==='source_ids'){record[key]=values.getAll(key).join(';');continue;}record[key]=String(value).trim();}
      if(kindSelect.value==='dataset'){record.dataset_name=record.name;record.source_ids=values.getAll('source_ids').join(';');delete record.name;}
      if(!record.id)record.id=(record.name||record.dataset_name).toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
      if(!record.id)throw new Error('Please enter a stable ID using lowercase letters, numbers and hyphens.');
      for(const key of ['link','documentation_url'])if(record[key]&&!safeURL(record[key]))throw new Error('Please use an http:// or https:// URL.');
      const conflict=entries.find(r=>r.kind===kindSelect.value&&r.id===record.id);
      if(values.get('action')==='add'&&conflict)throw new Error('This ID already exists. Choose “Update an existing entry” or enter another ID.');
      if(values.get('action')==='update'&&!conflict)throw new Error('No existing entry has this ID. Check the ID or choose “Add a new entry”.');
      return {kind:kindSelect.value,action:values.get('action'),record};
    }
    form.addEventListener('submit',event=>{
      event.preventDefault();
      try{proposal=collect();}catch(error){status.textContent=error.message;return;}
      document.getElementById('proposal-preview').textContent=JSON.stringify(proposal,null,2);
      document.getElementById('review-proposal').hidden=false;
      const title=`[Inventory ${proposal.action}] ${proposal.record.name||proposal.record.dataset_name}`;
      const body='## Inventory proposal\n\nPlease review the access conditions, evidence and metadata below before applying this proposal.\n\n```json\n'+JSON.stringify(proposal,null,2)+'\n```';
      const url=config.repository+'/issues/new?'+new URLSearchParams({title,body,template:'inventory-proposal.md'});
      const issue=document.getElementById('open-issue');issue.href=url;issue.hidden=url.length>7000;
      document.getElementById('long-proposal').hidden=url.length<=7000;
      status.textContent='Proposal prepared. Review it below, then open a GitHub issue to submit it. No information has been sent.';
      document.getElementById('review-proposal').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth',block:'start'});
    });
    form.addEventListener('input',()=>{proposal=null;document.getElementById('review-proposal').hidden=true;status.textContent='';});
    form.addEventListener('change',()=>{proposal=null;document.getElementById('review-proposal').hidden=true;});
    document.getElementById('download-proposal').addEventListener('click',()=>{if(!proposal)return;const url=URL.createObjectURL(new Blob([JSON.stringify(proposal,null,2)+'\n'],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download=`${proposal.kind}-${proposal.record.id}.json`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});
    document.getElementById('save-draft').addEventListener('click',()=>{try{const draft={};for(const el of form.elements)if(el.name)draft[el.name]=el.multiple?[...el.selectedOptions].map(o=>o.value):el.value;localStorage.setItem('digital-inventory-draft',JSON.stringify(draft));status.textContent='Draft saved in this browser on this device.';}catch{status.textContent='Your browser could not save this draft.';}});
    document.getElementById('restore-draft').addEventListener('click',()=>{try{const draft=JSON.parse(localStorage.getItem('digital-inventory-draft')||'null');if(!draft){status.textContent='No saved draft in this browser.';return;}for(const el of form.elements)if(el.name&&draft[el.name]!==undefined){if(el.multiple)[...el.options].forEach(o=>o.selected=draft[el.name].includes(o.value));else el.value=draft[el.name];}syncKind();document.getElementById('review-proposal').hidden=true;proposal=null;status.textContent='Draft restored. Review the fields before preparing your proposal.';}catch{status.textContent='Your browser could not restore this draft.';}});
  }
})();
