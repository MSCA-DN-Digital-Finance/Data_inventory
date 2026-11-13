# DIGITAL · Research Data Inventory

A research catalogue for the MSCA Digital Finance network: which data is available, how to access it, and what to know before using it.

The homepage lists data sources with a clickable subject cloud. Datasets have their own navigation tab and page. Both catalogues provide search, filters, shareable entry details, related providers and CSV downloads, alongside a contribution page. Access conditions come first, followed by formats, quality, publication lag, history, revisions and reuse restrictions. The supplied DIGITAL logo is the main brand; the EU funding logo appears in every page footer.

## Run locally

Python 3.9+ is the only build dependency.

```sh
python3 scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory _site
```

Open [the local preview](http://127.0.0.1:8000). Output is generated in `_site/` and is not committed. Relative links work at the GitHub project path and on a custom domain. No external fonts, analytics or client libraries are required.

## Publish on GitHub Pages

1. Push these changes to `main` (or merge a pull request).
2. In **Settings → Pages → Build and deployment → Source**, choose **GitHub Actions**.
3. Run **Validate and deploy inventory** from the Actions tab, or push a change to `main`.
4. The deployment environment reports the actual site URL. With the current repository name and no custom domain, the expected address is https://msca-dn-digital-finance.github.io/Data_inventory/.

The workflow validates data, builds and tests every pull request, and deploys only pushes to `main` or a manual run on `main`. GitHub may require an administrator to enable Pages or approve the `github-pages` environment. See [GitHub’s publishing-source guide](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) and [custom workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## CSV releases

[Inventory releases](https://github.com/MSCA-DN-Digital-Finance/Data_inventory/releases) provide versioned downloads of **both** `data-sources.csv` and `datasets.csv`, plus `SHA256SUMS.txt`. The `Publish inventory release` workflow runs after an approved proposal changes a CSV, for direct CSV pushes to `main`, or manually from Actions. Tags use `inventory-YYYY-MM-DD-<commit SHA prefix>` and release notes link to the exact source commit.

Approval-triggered releases use the applied commit, even if other changes reach `main` before the release runs. Approval no-ops are skipped. Reruns resume incomplete drafts or leave an already published snapshot unchanged. A manual run can create a snapshot of the current revision or a selected commit already on `main`. Releases never alter the CSVs or force-move tags.

## Maintain the inventory

- [Sources CSV](data/data-sources.csv): providers and platforms.
- [Datasets CSV](data/datasets.csv): specific prepared research datasets, extracts and panels.
- [Contribution and metadata guide](CONTRIBUTING.md): field definitions, evidence standards and importing proposals.
- `site/`: page templates, CSS and browser behavior.
- `site/config.json`: repository links and project configuration.
- `scripts/build_site.py`: CSV validation, generated JSON, no-JavaScript fallback and static packaging.

CSV files remain the canonical data. IDs are stable; names can change. Empty metadata is displayed as **Not yet documented**. Legacy fields remain available for compatibility. Most migrated notes are contributor reports, not newly verified access guarantees. Review dates are set only for specifically checked metadata.

The contribution page prepares a GitHub issue; the contributor reviews and submits it on GitHub. A maintainer reviews the proposal and adds the `inventory-approved` issue label. The approval workflow automatically validates it, updates the CSV and README, commits to `main`, starts a Pages deployment, and closes the issue with `inventory-applied`. No local commands are needed. The public form does not write directly to the repository or host credentials. A JSON download and local browser draft support longer or unfinished submissions. Automatic approval requires one fenced `json` proposal in the issue body; paste attachment-only JSON into the body before approval. See [maintainer review](CONTRIBUTING.md#maintainer-review) for retries and requirements.

```sh
python3 scripts/import_proposal.py /path/to/proposal.json          # validate / dry-run
python3 scripts/import_proposal.py /path/to/proposal.json --write  # apply reviewed change
python3 scripts/build_site.py
python3 -m unittest discover -s tests -v
python3 update_README.py
```

The existing README workflow refreshes only the generated fallback below. Introductory and maintenance text can be edited directly.

<details>
<summary>Browse the legacy inventory tables</summary>

<!-- BEGIN INVENTORY -->
## Table of Contents

- [Data Sources – Full List ](#data-sources-full-list)
- [Data Sources by Subject ](#data-sources-by-subject)
  - [banking ](#sources-banking)
  - [blockchain ](#sources-blockchain)
  - [credit ](#sources-credit)
  - [cryptocurrencies ](#sources-cryptocurrencies)
  - [economics ](#sources-economics)
  - [electricity ](#sources-electricity)
  - [emissions ](#sources-emissions)
  - [energy ](#sources-energy)
  - [finance ](#sources-finance)
  - [gas ](#sources-gas)
  - [macro-economy ](#sources-macro-economy)
  - [operations ](#sources-operations)
  - [population ](#sources-population)
  - [ready-to-use ](#sources-ready-to-use)
  - [regulation ](#sources-regulation)
- [Data Sources by IRP ](#data-sources-by-irp)
  - [IRP 14 ](#sources-14)
  - [IRP 15 ](#sources-15)
  - [IRP 15, 13 ](#sources-15, 13)
  - [IRP 15;13 ](#sources-15;13)
- [Datasets – Full List ](#datasets-full-list)
- [Datasets by Subject ](#datasets-by-subject)
  - [banking ](#sets-banking)
  - [blockchain ](#sets-blockchain)
  - [credit ](#sets-credit)
  - [cryptocurrencies ](#sets-cryptocurrencies)
  - [electricity ](#sets-electricity)
  - [energy ](#sets-energy)
  - [environment ](#sets-environment)
  - [finance ](#sets-finance)
  - [macro-economy ](#sets-macro-economy)
  - [microstructure ](#sets-microstructure)
  - [stablecoin ](#sets-stablecoin)
- [Datasets by IRP ](#datasets-by-irp)
  - [IRP 14 ](#sets-14)
  - [IRP 15 ](#sets-15)

---

## Data Sources – Full List <a name='data-sources-full-list'></a>

| Name | Short Description | Subject(s) | IRP | Link | Access | Collection |
|---|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | finance;banking;macro-economy;credit | 14 | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |
| Binance | Binance's free API allows collection of historical OHLC data for most pairs at high frequency | cryptocurrencies;finance | 14 | https://developers.binance.com/docs/binance-spot-api-docs/README | Public | API / free unlimited key |
| Bloomberg Terminal | Commercial terminal data; used for a direct-lending loan snapshot (current terms only, no history) | credit;finance;economics | 15, 13 | https://www.bloomberg.com/professional/products/bloomberg-terminal/ | Private - institutional licence | Terminal / licence |
| BRC | Blockchain Research center - data on demand, (cryptocurrencies, financial news, BTC futures...). | blockchain;cryptocurrencies;finance | 14 | https://data.blockchain-research-center.com/ | Private - accessible to IRPs | Email Request |
| Dune | Dune allows access to on-chain data including multiple pre-made queries about various DeFi projects | blockchain;cryptocurrencies;finance | 14 | https://dune.com/discover/content/favorites | Public | API / free limited key |
| ECB Data Portal | European Central Bank statistics: policy and money-market rates (€STR, EONIA, Euribor), HICP, euro-area yield curves, ECB Survey of Professional Forecasters, ECB Real-Time Database (vintages via includeHistory=true) | macro-economy;finance;banking | 15;13 | https://data.ecb.europa.eu | Public | API / open (SDMX REST) |
| EDW | Internal Enterprise Data Warehouse integrating core operational and financial systems | credit;operations;finance | 14 | https://eurodw.eu/?lang=it | Private | Database |
| EIA | U.S. Energy Information Administration – official energy data (generation, consumption, fuel, prices). | energy;electricity;gas | 14 | https://www.eia.gov/opendata/ | Public | API / free unlimited key |
| EPA | U.S. Environmental Protection Agency – environmental and emissions data relevant to power sector and fuels. | emissions;energy | 14 | https://www.epa.gov/data | Public | API / free unlimited key |
| Eurostat | EU-level statistics and macro-economic indicators (economy, population, employment...) | macro-economy;population | 14 | https://ec.europa.eu/eurostat/web/main/data/database | Public | API / open |
| Fed Board yield curve | Gürkaynak–Sack–Wright US Treasury zero-coupon curve and Svensson parameters, daily since 1961 | finance;macro-economy | 15 | https://www.federalreserve.gov/data/nominal-yield-curve.htm | Public | Direct download (csv) |
| FERC | U.S. Federal Energy Regulatory Commission – market, transmission, and financial filings for utilities. | energy;electricity;regulation | 14 | https://data.ferc.gov | Public | Bulk download / manual |
| FRED | Federal Reserve Economic Data - macro-economic time series data on US market | macro-economy;finance;population | 14 | https://fred.stlouisfed.org | Public | API / free unlimited key |
| ISTAT | Italian national statistics office (demography, employment, prices, national accounts...) | macro-economy;population | 14 | https://esploradati.istat.it/databrowser/ | Public | API / open |
| Kenneth French Data Library | Daily/monthly Fama–French factors, momentum and industry portfolio returns since 1926 | finance | 15 | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html | Public | Direct download (zip) |
| NERC | North American Electric Reliability Corporation – reliability standards, disturbances, and system performance data. | energy;electricity | 14 | https://www.nerc.com/ | Public | Reports (unstructured) / Direct Download |
| Philadelphia Fed RTDSM | Real-Time Data Set for Macroeconomists – every published vintage of US CPI, core CPI, payrolls, industrial production, unemployment and real GDP | macro-economy | 15 | https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/real-time-data-set-for-macroeconomists | Public | Direct download (xlsx) |
| Philadelphia Fed SPF | Survey of Professional Forecasters – quarterly US forecasts of inflation, unemployment, rates and output (human benchmark for forecasting models) | macro-economy | 15 | https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/survey-of-professional-forecasters | Public | Direct download (xlsx) |
| PUDL | Public Utility Data Liberation – cleaned, imputed, directly usable datasets derived mainly from EIA, FERC, EPA and SEC. | energy;electricity;emissions;ready-to-use | 14 | https://catalystcoop-pudl.readthedocs.io/en/latest/data_access.html | Public | Open S3 bucket / Zenodo direct download / Kaggle (colab) notebook |
| SEC BDC Data Sets | Quarterly XBRL extracts of business development company filings, including the schedule of investments (loan-level private-credit holdings, fair values, rates) | credit;finance;regulation | 15 | https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets | Public | Bulk download / quarterly zip (declare a User-Agent with contact email) |
| SEC Form N-PORT Data Sets | Quarterly fund holdings reports from 2019, with default, arrears and PIK flags on debt holdings | credit;finance;regulation | 15 | https://www.sec.gov/data-research/sec-markets-data/form-n-port-data-sets | Public | Bulk download / quarterly zip |
| Thegraph | TheGraph allows free access to curated datastreams on the blockchain - including on-chain data on popular DEFI protocols (uniswap,aave...) | blockchain;cryptocurrencies;credit | 14 | https://thegraph.com/explorer | Public | API / free limited key - requires base wallet |


## Data Sources by Subject <a name='data-sources-by-subject'></a>


### banking <a name='sources-banking'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | 14 | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |
| ECB Data Portal | European Central Bank statistics: policy and money-market rates (€STR, EONIA, Euribor), HICP, euro-area yield curves, ECB Survey of Professional Forecasters, ECB Real-Time Database (vintages via includeHistory=true) | 15;13 | https://data.ecb.europa.eu | Public | API / open (SDMX REST) |


### blockchain <a name='sources-blockchain'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| BRC | Blockchain Research center - data on demand, (cryptocurrencies, financial news, BTC futures...). | 14 | https://data.blockchain-research-center.com/ | Private - accessible to IRPs | Email Request |
| Dune | Dune allows access to on-chain data including multiple pre-made queries about various DeFi projects | 14 | https://dune.com/discover/content/favorites | Public | API / free limited key |
| Thegraph | TheGraph allows free access to curated datastreams on the blockchain - including on-chain data on popular DEFI protocols (uniswap,aave...) | 14 | https://thegraph.com/explorer | Public | API / free limited key - requires base wallet |


### credit <a name='sources-credit'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | 14 | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |
| Bloomberg Terminal | Commercial terminal data; used for a direct-lending loan snapshot (current terms only, no history) | 15, 13 | https://www.bloomberg.com/professional/products/bloomberg-terminal/ | Private - institutional licence | Terminal / licence |
| EDW | Internal Enterprise Data Warehouse integrating core operational and financial systems | 14 | https://eurodw.eu/?lang=it | Private | Database |
| SEC BDC Data Sets | Quarterly XBRL extracts of business development company filings, including the schedule of investments (loan-level private-credit holdings, fair values, rates) | 15 | https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets | Public | Bulk download / quarterly zip (declare a User-Agent with contact email) |
| SEC Form N-PORT Data Sets | Quarterly fund holdings reports from 2019, with default, arrears and PIK flags on debt holdings | 15 | https://www.sec.gov/data-research/sec-markets-data/form-n-port-data-sets | Public | Bulk download / quarterly zip |
| Thegraph | TheGraph allows free access to curated datastreams on the blockchain - including on-chain data on popular DEFI protocols (uniswap,aave...) | 14 | https://thegraph.com/explorer | Public | API / free limited key - requires base wallet |


### cryptocurrencies <a name='sources-cryptocurrencies'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Binance | Binance's free API allows collection of historical OHLC data for most pairs at high frequency | 14 | https://developers.binance.com/docs/binance-spot-api-docs/README | Public | API / free unlimited key |
| BRC | Blockchain Research center - data on demand, (cryptocurrencies, financial news, BTC futures...). | 14 | https://data.blockchain-research-center.com/ | Private - accessible to IRPs | Email Request |
| Dune | Dune allows access to on-chain data including multiple pre-made queries about various DeFi projects | 14 | https://dune.com/discover/content/favorites | Public | API / free limited key |
| Thegraph | TheGraph allows free access to curated datastreams on the blockchain - including on-chain data on popular DEFI protocols (uniswap,aave...) | 14 | https://thegraph.com/explorer | Public | API / free limited key - requires base wallet |


### economics <a name='sources-economics'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Bloomberg Terminal | Commercial terminal data; used for a direct-lending loan snapshot (current terms only, no history) | 15, 13 | https://www.bloomberg.com/professional/products/bloomberg-terminal/ | Private - institutional licence | Terminal / licence |


### electricity <a name='sources-electricity'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| EIA | U.S. Energy Information Administration – official energy data (generation, consumption, fuel, prices). | 14 | https://www.eia.gov/opendata/ | Public | API / free unlimited key |
| FERC | U.S. Federal Energy Regulatory Commission – market, transmission, and financial filings for utilities. | 14 | https://data.ferc.gov | Public | Bulk download / manual |
| NERC | North American Electric Reliability Corporation – reliability standards, disturbances, and system performance data. | 14 | https://www.nerc.com/ | Public | Reports (unstructured) / Direct Download |
| PUDL | Public Utility Data Liberation – cleaned, imputed, directly usable datasets derived mainly from EIA, FERC, EPA and SEC. | 14 | https://catalystcoop-pudl.readthedocs.io/en/latest/data_access.html | Public | Open S3 bucket / Zenodo direct download / Kaggle (colab) notebook |


### emissions <a name='sources-emissions'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| EPA | U.S. Environmental Protection Agency – environmental and emissions data relevant to power sector and fuels. | 14 | https://www.epa.gov/data | Public | API / free unlimited key |
| PUDL | Public Utility Data Liberation – cleaned, imputed, directly usable datasets derived mainly from EIA, FERC, EPA and SEC. | 14 | https://catalystcoop-pudl.readthedocs.io/en/latest/data_access.html | Public | Open S3 bucket / Zenodo direct download / Kaggle (colab) notebook |


### energy <a name='sources-energy'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| EIA | U.S. Energy Information Administration – official energy data (generation, consumption, fuel, prices). | 14 | https://www.eia.gov/opendata/ | Public | API / free unlimited key |
| EPA | U.S. Environmental Protection Agency – environmental and emissions data relevant to power sector and fuels. | 14 | https://www.epa.gov/data | Public | API / free unlimited key |
| FERC | U.S. Federal Energy Regulatory Commission – market, transmission, and financial filings for utilities. | 14 | https://data.ferc.gov | Public | Bulk download / manual |
| NERC | North American Electric Reliability Corporation – reliability standards, disturbances, and system performance data. | 14 | https://www.nerc.com/ | Public | Reports (unstructured) / Direct Download |
| PUDL | Public Utility Data Liberation – cleaned, imputed, directly usable datasets derived mainly from EIA, FERC, EPA and SEC. | 14 | https://catalystcoop-pudl.readthedocs.io/en/latest/data_access.html | Public | Open S3 bucket / Zenodo direct download / Kaggle (colab) notebook |


### finance <a name='sources-finance'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | 14 | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |
| Binance | Binance's free API allows collection of historical OHLC data for most pairs at high frequency | 14 | https://developers.binance.com/docs/binance-spot-api-docs/README | Public | API / free unlimited key |
| Bloomberg Terminal | Commercial terminal data; used for a direct-lending loan snapshot (current terms only, no history) | 15, 13 | https://www.bloomberg.com/professional/products/bloomberg-terminal/ | Private - institutional licence | Terminal / licence |
| BRC | Blockchain Research center - data on demand, (cryptocurrencies, financial news, BTC futures...). | 14 | https://data.blockchain-research-center.com/ | Private - accessible to IRPs | Email Request |
| Dune | Dune allows access to on-chain data including multiple pre-made queries about various DeFi projects | 14 | https://dune.com/discover/content/favorites | Public | API / free limited key |
| ECB Data Portal | European Central Bank statistics: policy and money-market rates (€STR, EONIA, Euribor), HICP, euro-area yield curves, ECB Survey of Professional Forecasters, ECB Real-Time Database (vintages via includeHistory=true) | 15;13 | https://data.ecb.europa.eu | Public | API / open (SDMX REST) |
| EDW | Internal Enterprise Data Warehouse integrating core operational and financial systems | 14 | https://eurodw.eu/?lang=it | Private | Database |
| Fed Board yield curve | Gürkaynak–Sack–Wright US Treasury zero-coupon curve and Svensson parameters, daily since 1961 | 15 | https://www.federalreserve.gov/data/nominal-yield-curve.htm | Public | Direct download (csv) |
| FRED | Federal Reserve Economic Data - macro-economic time series data on US market | 14 | https://fred.stlouisfed.org | Public | API / free unlimited key |
| Kenneth French Data Library | Daily/monthly Fama–French factors, momentum and industry portfolio returns since 1926 | 15 | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html | Public | Direct download (zip) |
| SEC BDC Data Sets | Quarterly XBRL extracts of business development company filings, including the schedule of investments (loan-level private-credit holdings, fair values, rates) | 15 | https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets | Public | Bulk download / quarterly zip (declare a User-Agent with contact email) |
| SEC Form N-PORT Data Sets | Quarterly fund holdings reports from 2019, with default, arrears and PIK flags on debt holdings | 15 | https://www.sec.gov/data-research/sec-markets-data/form-n-port-data-sets | Public | Bulk download / quarterly zip |


### gas <a name='sources-gas'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| EIA | U.S. Energy Information Administration – official energy data (generation, consumption, fuel, prices). | 14 | https://www.eia.gov/opendata/ | Public | API / free unlimited key |


### macro-economy <a name='sources-macro-economy'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | 14 | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |
| ECB Data Portal | European Central Bank statistics: policy and money-market rates (€STR, EONIA, Euribor), HICP, euro-area yield curves, ECB Survey of Professional Forecasters, ECB Real-Time Database (vintages via includeHistory=true) | 15;13 | https://data.ecb.europa.eu | Public | API / open (SDMX REST) |
| Eurostat | EU-level statistics and macro-economic indicators (economy, population, employment...) | 14 | https://ec.europa.eu/eurostat/web/main/data/database | Public | API / open |
| Fed Board yield curve | Gürkaynak–Sack–Wright US Treasury zero-coupon curve and Svensson parameters, daily since 1961 | 15 | https://www.federalreserve.gov/data/nominal-yield-curve.htm | Public | Direct download (csv) |
| FRED | Federal Reserve Economic Data - macro-economic time series data on US market | 14 | https://fred.stlouisfed.org | Public | API / free unlimited key |
| ISTAT | Italian national statistics office (demography, employment, prices, national accounts...) | 14 | https://esploradati.istat.it/databrowser/ | Public | API / open |
| Philadelphia Fed RTDSM | Real-Time Data Set for Macroeconomists – every published vintage of US CPI, core CPI, payrolls, industrial production, unemployment and real GDP | 15 | https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/real-time-data-set-for-macroeconomists | Public | Direct download (xlsx) |
| Philadelphia Fed SPF | Survey of Professional Forecasters – quarterly US forecasts of inflation, unemployment, rates and output (human benchmark for forecasting models) | 15 | https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/survey-of-professional-forecasters | Public | Direct download (xlsx) |


### operations <a name='sources-operations'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| EDW | Internal Enterprise Data Warehouse integrating core operational and financial systems | 14 | https://eurodw.eu/?lang=it | Private | Database |


### population <a name='sources-population'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Eurostat | EU-level statistics and macro-economic indicators (economy, population, employment...) | 14 | https://ec.europa.eu/eurostat/web/main/data/database | Public | API / open |
| FRED | Federal Reserve Economic Data - macro-economic time series data on US market | 14 | https://fred.stlouisfed.org | Public | API / free unlimited key |
| ISTAT | Italian national statistics office (demography, employment, prices, national accounts...) | 14 | https://esploradati.istat.it/databrowser/ | Public | API / open |


### ready-to-use <a name='sources-ready-to-use'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| PUDL | Public Utility Data Liberation – cleaned, imputed, directly usable datasets derived mainly from EIA, FERC, EPA and SEC. | 14 | https://catalystcoop-pudl.readthedocs.io/en/latest/data_access.html | Public | Open S3 bucket / Zenodo direct download / Kaggle (colab) notebook |


### regulation <a name='sources-regulation'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| FERC | U.S. Federal Energy Regulatory Commission – market, transmission, and financial filings for utilities. | 14 | https://data.ferc.gov | Public | Bulk download / manual |
| SEC BDC Data Sets | Quarterly XBRL extracts of business development company filings, including the schedule of investments (loan-level private-credit holdings, fair values, rates) | 15 | https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets | Public | Bulk download / quarterly zip (declare a User-Agent with contact email) |
| SEC Form N-PORT Data Sets | Quarterly fund holdings reports from 2019, with default, arrears and PIK flags on debt holdings | 15 | https://www.sec.gov/data-research/sec-markets-data/form-n-port-data-sets | Public | Bulk download / quarterly zip |


## Data Sources by IRP <a name='data-sources-by-irp'></a>


### IRP 14 <a name='sources-14'></a>

| Name | Short Description | Subject(s) | Link | Access | Collection |
|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | finance;banking;macro-economy;credit | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |
| Binance | Binance's free API allows collection of historical OHLC data for most pairs at high frequency | cryptocurrencies;finance | https://developers.binance.com/docs/binance-spot-api-docs/README | Public | API / free unlimited key |
| BRC | Blockchain Research center - data on demand, (cryptocurrencies, financial news, BTC futures...). | blockchain;cryptocurrencies;finance | https://data.blockchain-research-center.com/ | Private - accessible to IRPs | Email Request |
| Dune | Dune allows access to on-chain data including multiple pre-made queries about various DeFi projects | blockchain;cryptocurrencies;finance | https://dune.com/discover/content/favorites | Public | API / free limited key |
| EDW | Internal Enterprise Data Warehouse integrating core operational and financial systems | credit;operations;finance | https://eurodw.eu/?lang=it | Private | Database |
| EIA | U.S. Energy Information Administration – official energy data (generation, consumption, fuel, prices). | energy;electricity;gas | https://www.eia.gov/opendata/ | Public | API / free unlimited key |
| EPA | U.S. Environmental Protection Agency – environmental and emissions data relevant to power sector and fuels. | emissions;energy | https://www.epa.gov/data | Public | API / free unlimited key |
| Eurostat | EU-level statistics and macro-economic indicators (economy, population, employment...) | macro-economy;population | https://ec.europa.eu/eurostat/web/main/data/database | Public | API / open |
| FERC | U.S. Federal Energy Regulatory Commission – market, transmission, and financial filings for utilities. | energy;electricity;regulation | https://data.ferc.gov | Public | Bulk download / manual |
| FRED | Federal Reserve Economic Data - macro-economic time series data on US market | macro-economy;finance;population | https://fred.stlouisfed.org | Public | API / free unlimited key |
| ISTAT | Italian national statistics office (demography, employment, prices, national accounts...) | macro-economy;population | https://esploradati.istat.it/databrowser/ | Public | API / open |
| NERC | North American Electric Reliability Corporation – reliability standards, disturbances, and system performance data. | energy;electricity | https://www.nerc.com/ | Public | Reports (unstructured) / Direct Download |
| PUDL | Public Utility Data Liberation – cleaned, imputed, directly usable datasets derived mainly from EIA, FERC, EPA and SEC. | energy;electricity;emissions;ready-to-use | https://catalystcoop-pudl.readthedocs.io/en/latest/data_access.html | Public | Open S3 bucket / Zenodo direct download / Kaggle (colab) notebook |
| Thegraph | TheGraph allows free access to curated datastreams on the blockchain - including on-chain data on popular DEFI protocols (uniswap,aave...) | blockchain;cryptocurrencies;credit | https://thegraph.com/explorer | Public | API / free limited key - requires base wallet |


### IRP 15 <a name='sources-15'></a>

| Name | Short Description | Subject(s) | Link | Access | Collection |
|---|---|---|---|---|---|
| Fed Board yield curve | Gürkaynak–Sack–Wright US Treasury zero-coupon curve and Svensson parameters, daily since 1961 | finance;macro-economy | https://www.federalreserve.gov/data/nominal-yield-curve.htm | Public | Direct download (csv) |
| Kenneth French Data Library | Daily/monthly Fama–French factors, momentum and industry portfolio returns since 1926 | finance | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html | Public | Direct download (zip) |
| Philadelphia Fed RTDSM | Real-Time Data Set for Macroeconomists – every published vintage of US CPI, core CPI, payrolls, industrial production, unemployment and real GDP | macro-economy | https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/real-time-data-set-for-macroeconomists | Public | Direct download (xlsx) |
| Philadelphia Fed SPF | Survey of Professional Forecasters – quarterly US forecasts of inflation, unemployment, rates and output (human benchmark for forecasting models) | macro-economy | https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/survey-of-professional-forecasters | Public | Direct download (xlsx) |
| SEC BDC Data Sets | Quarterly XBRL extracts of business development company filings, including the schedule of investments (loan-level private-credit holdings, fair values, rates) | credit;finance;regulation | https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets | Public | Bulk download / quarterly zip (declare a User-Agent with contact email) |
| SEC Form N-PORT Data Sets | Quarterly fund holdings reports from 2019, with default, arrears and PIK flags on debt holdings | credit;finance;regulation | https://www.sec.gov/data-research/sec-markets-data/form-n-port-data-sets | Public | Bulk download / quarterly zip |


### IRP 15, 13 <a name='sources-15, 13'></a>

| Name | Short Description | Subject(s) | Link | Access | Collection |
|---|---|---|---|---|---|
| Bloomberg Terminal | Commercial terminal data; used for a direct-lending loan snapshot (current terms only, no history) | credit;finance;economics | https://www.bloomberg.com/professional/products/bloomberg-terminal/ | Private - institutional licence | Terminal / licence |


### IRP 15;13 <a name='sources-15;13'></a>

| Name | Short Description | Subject(s) | Link | Access | Collection |
|---|---|---|---|---|---|
| ECB Data Portal | European Central Bank statistics: policy and money-market rates (€STR, EONIA, Euribor), HICP, euro-area yield curves, ECB Survey of Professional Forecasters, ECB Real-Time Database (vintages via includeHistory=true) | macro-economy;finance;banking | https://data.ecb.europa.eu | Public | API / open (SDMX REST) |

---

## Datasets – Full List <a name='datasets-full-list'></a>

| Dataset Name | Short Description | Subject(s) | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|---|
| BI_bad_loans | Bank of Italy table, data on bad loan amounts, by region and sector in Italy | credit;banking | 14 | Monthly | 2011 | updated with 3 months lag | Some missing values | Ask |
| BI_loan_origination | Bank of Italy table 20224 contains data on loan origination, excluding bad loans, by region and sector in Italy | credit;banking | 14 | Monthly | 2011 | updated with 3 months lag | Clean | Ask |
| BI_nace | Bank of Italy data on loan origination, by NACE classification and sector, Italy level only | credit;banking | 14 | Monthly | 2006 | updated with 3 months lag | Some missing values | Ask |
| EIA_923 | EIA form 923 contains monthly data on power generation in US, including net generation, fuel receipts and retail sales by state. | electricity;energy | 14 | Monthly | 2001 | up-to-date | Some missing values | Ask |
| EIA_930 | EIA form 930 contains operational data of the american electricity grid including demand, demand forecast and generation by balancing authority. | electricity | 14 | Hourly | 2019 | up-to-date | Some missing values | Download parquet from PUDL |
| EIA_capacity | Capacity data aggregated from EIA plant-level dataset, infering capacity from nameplate capacity of all operating plants within each balancing authority. | energy;electricity | 14 | Yearly | 2001 | 2025 | Clean | Ask |
| EIA_outlook | EIA Annual Energy Outlook provides projection of future energy variables including prices,load and generation based on 11 scenarios. The forecast method is open-source | energy;electricity;macro-economy | 14 | Yearly | 2023 | 2050 | Clean | Ask |
| EPA_CEMS | hourly continuous emissions monitoring system data. CO2,SO2,NOx emissions, plant level granularity. | energy;environment | 14 | Hourly | 1995 | up-to-date | Clean | Download parquet from PUDL |
| Macro_realtime_data_layer | Validated real-time macro data layer for forecasting rates, inflation and unemployment in the US, euro area and Italy: 27 datasets, 1,060 series, real-time vintages (RTDSM, ECB RTD), US and ECB SPF. Data as Parquet files, with code, catalogue and validation report: https://github.com/MSCA-DN-Digital-Finance/macro-realtime-data | macro-economy;finance | 15 | Daily / Monthly / Quarterly | 1854 | up-to-date | Clean (133/133 automated checks incl. exact cross-source matches) | Download Parquet from GitHub (data/public) |
| SEC_BDC_loan_quarter_panel | Loan × lender × quarter private-credit panel rebuilt from the SEC BDC Data Sets schedules of investments: 194,351 holding-quarters, 128 BDCs; filings kept only if holdings reconcile to reported totals, loans linked across quarters only when unambiguous | credit;finance | 15 | Quarterly | 2022 | 2026 | Clean (verified reconciliation) | Ask |
| Stablecoin DeFi Dataset | This dataset contains features collected from onchain sources regarding the stability of stablecoins. The main focus is USDT and USDC, the dataset aims to provide a granular and complete view of the microstructure conditions governing the stability of these assets. | stablecoin;blockchain;finance;microstructure | 14 | Hourly | 01-01-2022 | Continuously updated | No missing values, timestamp aligned on ethereum blocks. The hourly observed data is queried on the first block closed in that given hour, this time can vary by around 12 seconds based on the ETH blockchain block time. | bulk download |
| Uniswap_hourly_metrics | hourly set of metrics on largest uniswap stablecoin pools, includes prices and aggregated net per-token swaps at all fee tiers | blockchain;cryptocurrencies | 14 | Hourly | 2021 | up-to-date | Clean | Ask-to be added to BRC dataset |


## Datasets by Subject <a name='datasets-by-subject'></a>


### banking <a name='sets-banking'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| BI_bad_loans | Bank of Italy table, data on bad loan amounts, by region and sector in Italy | 14 | Monthly | 2011 | updated with 3 months lag | Some missing values | Ask |
| BI_loan_origination | Bank of Italy table 20224 contains data on loan origination, excluding bad loans, by region and sector in Italy | 14 | Monthly | 2011 | updated with 3 months lag | Clean | Ask |
| BI_nace | Bank of Italy data on loan origination, by NACE classification and sector, Italy level only | 14 | Monthly | 2006 | updated with 3 months lag | Some missing values | Ask |


### blockchain <a name='sets-blockchain'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| Stablecoin DeFi Dataset | This dataset contains features collected from onchain sources regarding the stability of stablecoins. The main focus is USDT and USDC, the dataset aims to provide a granular and complete view of the microstructure conditions governing the stability of these assets. | 14 | Hourly | 01-01-2022 | Continuously updated | No missing values, timestamp aligned on ethereum blocks. The hourly observed data is queried on the first block closed in that given hour, this time can vary by around 12 seconds based on the ETH blockchain block time. | bulk download |
| Uniswap_hourly_metrics | hourly set of metrics on largest uniswap stablecoin pools, includes prices and aggregated net per-token swaps at all fee tiers | 14 | Hourly | 2021 | up-to-date | Clean | Ask-to be added to BRC dataset |


### credit <a name='sets-credit'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| BI_bad_loans | Bank of Italy table, data on bad loan amounts, by region and sector in Italy | 14 | Monthly | 2011 | updated with 3 months lag | Some missing values | Ask |
| BI_loan_origination | Bank of Italy table 20224 contains data on loan origination, excluding bad loans, by region and sector in Italy | 14 | Monthly | 2011 | updated with 3 months lag | Clean | Ask |
| BI_nace | Bank of Italy data on loan origination, by NACE classification and sector, Italy level only | 14 | Monthly | 2006 | updated with 3 months lag | Some missing values | Ask |
| SEC_BDC_loan_quarter_panel | Loan × lender × quarter private-credit panel rebuilt from the SEC BDC Data Sets schedules of investments: 194,351 holding-quarters, 128 BDCs; filings kept only if holdings reconcile to reported totals, loans linked across quarters only when unambiguous | 15 | Quarterly | 2022 | 2026 | Clean (verified reconciliation) | Ask |


### cryptocurrencies <a name='sets-cryptocurrencies'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| Uniswap_hourly_metrics | hourly set of metrics on largest uniswap stablecoin pools, includes prices and aggregated net per-token swaps at all fee tiers | 14 | Hourly | 2021 | up-to-date | Clean | Ask-to be added to BRC dataset |


### electricity <a name='sets-electricity'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| EIA_923 | EIA form 923 contains monthly data on power generation in US, including net generation, fuel receipts and retail sales by state. | 14 | Monthly | 2001 | up-to-date | Some missing values | Ask |
| EIA_930 | EIA form 930 contains operational data of the american electricity grid including demand, demand forecast and generation by balancing authority. | 14 | Hourly | 2019 | up-to-date | Some missing values | Download parquet from PUDL |
| EIA_capacity | Capacity data aggregated from EIA plant-level dataset, infering capacity from nameplate capacity of all operating plants within each balancing authority. | 14 | Yearly | 2001 | 2025 | Clean | Ask |
| EIA_outlook | EIA Annual Energy Outlook provides projection of future energy variables including prices,load and generation based on 11 scenarios. The forecast method is open-source | 14 | Yearly | 2023 | 2050 | Clean | Ask |


### energy <a name='sets-energy'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| EIA_923 | EIA form 923 contains monthly data on power generation in US, including net generation, fuel receipts and retail sales by state. | 14 | Monthly | 2001 | up-to-date | Some missing values | Ask |
| EIA_capacity | Capacity data aggregated from EIA plant-level dataset, infering capacity from nameplate capacity of all operating plants within each balancing authority. | 14 | Yearly | 2001 | 2025 | Clean | Ask |
| EIA_outlook | EIA Annual Energy Outlook provides projection of future energy variables including prices,load and generation based on 11 scenarios. The forecast method is open-source | 14 | Yearly | 2023 | 2050 | Clean | Ask |
| EPA_CEMS | hourly continuous emissions monitoring system data. CO2,SO2,NOx emissions, plant level granularity. | 14 | Hourly | 1995 | up-to-date | Clean | Download parquet from PUDL |


### environment <a name='sets-environment'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| EPA_CEMS | hourly continuous emissions monitoring system data. CO2,SO2,NOx emissions, plant level granularity. | 14 | Hourly | 1995 | up-to-date | Clean | Download parquet from PUDL |


### finance <a name='sets-finance'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| Macro_realtime_data_layer | Validated real-time macro data layer for forecasting rates, inflation and unemployment in the US, euro area and Italy: 27 datasets, 1,060 series, real-time vintages (RTDSM, ECB RTD), US and ECB SPF. Data as Parquet files, with code, catalogue and validation report: https://github.com/MSCA-DN-Digital-Finance/macro-realtime-data | 15 | Daily / Monthly / Quarterly | 1854 | up-to-date | Clean (133/133 automated checks incl. exact cross-source matches) | Download Parquet from GitHub (data/public) |
| SEC_BDC_loan_quarter_panel | Loan × lender × quarter private-credit panel rebuilt from the SEC BDC Data Sets schedules of investments: 194,351 holding-quarters, 128 BDCs; filings kept only if holdings reconcile to reported totals, loans linked across quarters only when unambiguous | 15 | Quarterly | 2022 | 2026 | Clean (verified reconciliation) | Ask |
| Stablecoin DeFi Dataset | This dataset contains features collected from onchain sources regarding the stability of stablecoins. The main focus is USDT and USDC, the dataset aims to provide a granular and complete view of the microstructure conditions governing the stability of these assets. | 14 | Hourly | 01-01-2022 | Continuously updated | No missing values, timestamp aligned on ethereum blocks. The hourly observed data is queried on the first block closed in that given hour, this time can vary by around 12 seconds based on the ETH blockchain block time. | bulk download |


### macro-economy <a name='sets-macro-economy'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| EIA_outlook | EIA Annual Energy Outlook provides projection of future energy variables including prices,load and generation based on 11 scenarios. The forecast method is open-source | 14 | Yearly | 2023 | 2050 | Clean | Ask |
| Macro_realtime_data_layer | Validated real-time macro data layer for forecasting rates, inflation and unemployment in the US, euro area and Italy: 27 datasets, 1,060 series, real-time vintages (RTDSM, ECB RTD), US and ECB SPF. Data as Parquet files, with code, catalogue and validation report: https://github.com/MSCA-DN-Digital-Finance/macro-realtime-data | 15 | Daily / Monthly / Quarterly | 1854 | up-to-date | Clean (133/133 automated checks incl. exact cross-source matches) | Download Parquet from GitHub (data/public) |


### microstructure <a name='sets-microstructure'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| Stablecoin DeFi Dataset | This dataset contains features collected from onchain sources regarding the stability of stablecoins. The main focus is USDT and USDC, the dataset aims to provide a granular and complete view of the microstructure conditions governing the stability of these assets. | 14 | Hourly | 01-01-2022 | Continuously updated | No missing values, timestamp aligned on ethereum blocks. The hourly observed data is queried on the first block closed in that given hour, this time can vary by around 12 seconds based on the ETH blockchain block time. | bulk download |


### stablecoin <a name='sets-stablecoin'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| Stablecoin DeFi Dataset | This dataset contains features collected from onchain sources regarding the stability of stablecoins. The main focus is USDT and USDC, the dataset aims to provide a granular and complete view of the microstructure conditions governing the stability of these assets. | 14 | Hourly | 01-01-2022 | Continuously updated | No missing values, timestamp aligned on ethereum blocks. The hourly observed data is queried on the first block closed in that given hour, this time can vary by around 12 seconds based on the ETH blockchain block time. | bulk download |


## Datasets by IRP <a name='datasets-by-irp'></a>


### IRP 14 <a name='sets-14'></a>

| Dataset Name | Short Description | Subject(s) | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| BI_bad_loans | Bank of Italy table, data on bad loan amounts, by region and sector in Italy | credit;banking | Monthly | 2011 | updated with 3 months lag | Some missing values | Ask |
| BI_loan_origination | Bank of Italy table 20224 contains data on loan origination, excluding bad loans, by region and sector in Italy | credit;banking | Monthly | 2011 | updated with 3 months lag | Clean | Ask |
| BI_nace | Bank of Italy data on loan origination, by NACE classification and sector, Italy level only | credit;banking | Monthly | 2006 | updated with 3 months lag | Some missing values | Ask |
| EIA_923 | EIA form 923 contains monthly data on power generation in US, including net generation, fuel receipts and retail sales by state. | electricity;energy | Monthly | 2001 | up-to-date | Some missing values | Ask |
| EIA_930 | EIA form 930 contains operational data of the american electricity grid including demand, demand forecast and generation by balancing authority. | electricity | Hourly | 2019 | up-to-date | Some missing values | Download parquet from PUDL |
| EIA_capacity | Capacity data aggregated from EIA plant-level dataset, infering capacity from nameplate capacity of all operating plants within each balancing authority. | energy;electricity | Yearly | 2001 | 2025 | Clean | Ask |
| EIA_outlook | EIA Annual Energy Outlook provides projection of future energy variables including prices,load and generation based on 11 scenarios. The forecast method is open-source | energy;electricity;macro-economy | Yearly | 2023 | 2050 | Clean | Ask |
| EPA_CEMS | hourly continuous emissions monitoring system data. CO2,SO2,NOx emissions, plant level granularity. | energy;environment | Hourly | 1995 | up-to-date | Clean | Download parquet from PUDL |
| Stablecoin DeFi Dataset | This dataset contains features collected from onchain sources regarding the stability of stablecoins. The main focus is USDT and USDC, the dataset aims to provide a granular and complete view of the microstructure conditions governing the stability of these assets. | stablecoin;blockchain;finance;microstructure | Hourly | 01-01-2022 | Continuously updated | No missing values, timestamp aligned on ethereum blocks. The hourly observed data is queried on the first block closed in that given hour, this time can vary by around 12 seconds based on the ETH blockchain block time. | bulk download |
| Uniswap_hourly_metrics | hourly set of metrics on largest uniswap stablecoin pools, includes prices and aggregated net per-token swaps at all fee tiers | blockchain;cryptocurrencies | Hourly | 2021 | up-to-date | Clean | Ask-to be added to BRC dataset |


### IRP 15 <a name='sets-15'></a>

| Dataset Name | Short Description | Subject(s) | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| Macro_realtime_data_layer | Validated real-time macro data layer for forecasting rates, inflation and unemployment in the US, euro area and Italy: 27 datasets, 1,060 series, real-time vintages (RTDSM, ECB RTD), US and ECB SPF. Data as Parquet files, with code, catalogue and validation report: https://github.com/MSCA-DN-Digital-Finance/macro-realtime-data | macro-economy;finance | Daily / Monthly / Quarterly | 1854 | up-to-date | Clean (133/133 automated checks incl. exact cross-source matches) | Download Parquet from GitHub (data/public) |
| SEC_BDC_loan_quarter_panel | Loan × lender × quarter private-credit panel rebuilt from the SEC BDC Data Sets schedules of investments: 194,351 holding-quarters, 128 BDCs; filings kept only if holdings reconcile to reported totals, loans linked across quarters only when unambiguous | credit;finance | Quarterly | 2022 | 2026 | Clean (verified reconciliation) | Ask |
<!-- END INVENTORY -->

</details>
