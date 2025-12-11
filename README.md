# MSCA DIGITAL - 🗂 Data Inventory

This repository is meant to host a list of relevant data sources and datasets found and used by IRPs. 

IRPs are welcome to add their contributions in the following csv files :


- [List of datasets](./data/datasets.csv) 
- [List of data sources](./data/data-sources.csv)

The README is automatically generated, please do not edit it directly. 

<!-- BEGIN INVENTORY -->
## Table of Contents

- [Data Sources – Full List ](#data-sources-full-list)
- [Data Sources by Subject ](#data-sources-by-subject)
  - [banking ](#sources-banking)
  - [blockchain ](#sources-blockchain)
  - [credit ](#sources-credit)
  - [cryptocurrencies ](#sources-cryptocurrencies)
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
- [Datasets – Full List ](#datasets-full-list)
- [Datasets by Subject ](#datasets-by-subject)
  - [banking ](#sets-banking)
  - [credit ](#sets-credit)
  - [electricity ](#sets-electricity)
  - [energy ](#sets-energy)
- [Datasets by IRP ](#datasets-by-irp)
  - [IRP 14 ](#sets-14)

---

## Data Sources – Full List <a name='data-sources-full-list'></a>

| Name | Short Description | Subject(s) | IRP | Link | Access | Collection |
|---|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | finance;banking;macro-economy;credit | 14 | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |
| Binance | Binance's free API allows collection of historical OHLC data for most pairs at high frequency | cryptocurrencies;finance | 14 | https://developers.binance.com/docs/binance-spot-api-docs/README | Public | API / free unllimited key |
| BRC | Blockchain Research center - data on demand, (cryptocurrencies, financial news, BTC futures...). | blockchain;cryptocurrencies;finance | 14 | https://data.blockchain-research-center.com/ | Private - accessible to IRPs | Email Request |
| EDW | Internal Enterprise Data Warehouse integrating core operational and financial systems | credit;operations;finance | 14 | https://eurodw.eu/?lang=it | Private | Database |
| EIA | U.S. Energy Information Administration – official energy data (generation, consumption, fuel, prices). | energy;electricity;gas | 14 | https://www.eia.gov/opendata/ | Public | API / free unlimited key |
| EPA | U.S. Environmental Protection Agency – environmental and emissions data relevant to power sector and fuels. | emissions;energy | 14 | https://www.epa.gov/data | Public | API / free unlimited key |
| Eurostat | EU-level statistics and macro-economic indicators (economy, population, employment...) | macro-economy;population | 14 | https://ec.europa.eu/eurostat/web/main/data/database | Public | API / open |
| FERC | U.S. Federal Energy Regulatory Commission – market, transmission, and financial filings for utilities. | energy;electricity;regulation | 14 | https://data.ferc.gov | Public | Bulk download / manual |
| FRED | Federal Reserve Economic Data - macro-economic time series data on US market | macro-economy;finance;population | 14 | https://fred.stlouisfed.org | Public | API / free unlimited key |
| ISTAT | Italian national statistics office (demography, employment, prices, national accounts...) | macro-economy;population | 14 | https://esploradati.istat.it/databrowser/ | Public | API / open |
| NERC | North American Electric Reliability Corporation – reliability standards, disturbances, and system performance data. | energy;electricity | 14 | https://www.nerc.com/ | Public | Reports (unstructured) / Direct Download |
| PUDL | Public Utility Data Liberation – cleaned, imputed, directly usable datasets derived mainly from EIA, FERC, EPA and SEC. | energy;electricity;emissions;ready-to-use | 14 | https://catalystcoop-pudl.readthedocs.io/en/latest/data_access.html | Public | Open S3 bucket / Zenodo direct download / Kaggle (colab) notebook |
| Thegraph | TheGraph allows free access to curated datastreams on the blockchain - including on-chain data on popular DEFI protocols (uniswap,aave...) | blockchain;cryptocurrencies;credit | 14 | https://thegraph.com/explorer | Public | API / free limited key - requires base wallet |


## Data Sources by Subject <a name='data-sources-by-subject'></a>


### banking <a name='sources-banking'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | 14 | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |


### blockchain <a name='sources-blockchain'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| BRC | Blockchain Research center - data on demand, (cryptocurrencies, financial news, BTC futures...). | 14 | https://data.blockchain-research-center.com/ | Private - accessible to IRPs | Email Request |
| Thegraph | TheGraph allows free access to curated datastreams on the blockchain - including on-chain data on popular DEFI protocols (uniswap,aave...) | 14 | https://thegraph.com/explorer | Public | API / free limited key - requires base wallet |


### credit <a name='sources-credit'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | 14 | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |
| EDW | Internal Enterprise Data Warehouse integrating core operational and financial systems | 14 | https://eurodw.eu/?lang=it | Private | Database |
| Thegraph | TheGraph allows free access to curated datastreams on the blockchain - including on-chain data on popular DEFI protocols (uniswap,aave...) | 14 | https://thegraph.com/explorer | Public | API / free limited key - requires base wallet |


### cryptocurrencies <a name='sources-cryptocurrencies'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Binance | Binance's free API allows collection of historical OHLC data for most pairs at high frequency | 14 | https://developers.binance.com/docs/binance-spot-api-docs/README | Public | API / free unllimited key |
| BRC | Blockchain Research center - data on demand, (cryptocurrencies, financial news, BTC futures...). | 14 | https://data.blockchain-research-center.com/ | Private - accessible to IRPs | Email Request |
| Thegraph | TheGraph allows free access to curated datastreams on the blockchain - including on-chain data on popular DEFI protocols (uniswap,aave...) | 14 | https://thegraph.com/explorer | Public | API / free limited key - requires base wallet |


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
| Binance | Binance's free API allows collection of historical OHLC data for most pairs at high frequency | 14 | https://developers.binance.com/docs/binance-spot-api-docs/README | Public | API / free unllimited key |
| BRC | Blockchain Research center - data on demand, (cryptocurrencies, financial news, BTC futures...). | 14 | https://data.blockchain-research-center.com/ | Private - accessible to IRPs | Email Request |
| EDW | Internal Enterprise Data Warehouse integrating core operational and financial systems | 14 | https://eurodw.eu/?lang=it | Private | Database |
| FRED | Federal Reserve Economic Data - macro-economic time series data on US market | 14 | https://fred.stlouisfed.org | Public | API / free unlimited key |


### gas <a name='sources-gas'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| EIA | U.S. Energy Information Administration – official energy data (generation, consumption, fuel, prices). | 14 | https://www.eia.gov/opendata/ | Public | API / free unlimited key |


### macro-economy <a name='sources-macro-economy'></a>

| Name | Short Description | IRP | Link | Access | Collection |
|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | 14 | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |
| Eurostat | EU-level statistics and macro-economic indicators (economy, population, employment...) | 14 | https://ec.europa.eu/eurostat/web/main/data/database | Public | API / open |
| FRED | Federal Reserve Economic Data - macro-economic time series data on US market | 14 | https://fred.stlouisfed.org | Public | API / free unlimited key |
| ISTAT | Italian national statistics office (demography, employment, prices, national accounts...) | 14 | https://esploradati.istat.it/databrowser/ | Public | API / open |


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


## Data Sources by IRP <a name='data-sources-by-irp'></a>


### IRP 14 <a name='sources-14'></a>

| Name | Short Description | Subject(s) | Link | Access | Collection |
|---|---|---|---|---|---|
| Banca d'Italia | Data from the Italian central bank (monetary, financial, balance of payments, banking system) | finance;banking;macro-economy;credit | https://infostat.bancaditalia.it/inquiry/home?spyglass/taxo:CUBESET=&ITEMSELEZ=&OPEN=true/&ep:LC=EN&COMM=BANKITALIA&ENV=LIVE&CTX=DIFF&IDX=1&/view:CUBEIDS=&graphMode= | Public | API / open |
| Binance | Binance's free API allows collection of historical OHLC data for most pairs at high frequency | cryptocurrencies;finance | https://developers.binance.com/docs/binance-spot-api-docs/README | Public | API / free unllimited key |
| BRC | Blockchain Research center - data on demand, (cryptocurrencies, financial news, BTC futures...). | blockchain;cryptocurrencies;finance | https://data.blockchain-research-center.com/ | Private - accessible to IRPs | Email Request |
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

---

## Datasets – Full List <a name='datasets-full-list'></a>

| Dataset Name | Short Description | Subject(s) | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|---|
| BI_TDB20224 | Bank of Italy table 20224 contains data on loan origination, excluding bad loans, by region and sector in Italy | credit;banking | 14 | Monthly | 2011 | updated with 3 months lag | Clean | Ask |
| EIA_923 | EIA form 923 contains monthly data on power generation in US, including net generation, fuel receipts and retail sales by state. | electricity;energy | 14 | Monthly | 2001 | up-to-date | Some missing values | Ask |
| EIA_930 | EIA form 930 contains operational data of the american electricity grid including demand, demand forecast and generation by balancing authority. | electricity | 14 | Hourly | 2019 | up-to-date | Some missing values | Download parquet from PUDL |


## Datasets by Subject <a name='datasets-by-subject'></a>


### banking <a name='sets-banking'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| BI_TDB20224 | Bank of Italy table 20224 contains data on loan origination, excluding bad loans, by region and sector in Italy | 14 | Monthly | 2011 | updated with 3 months lag | Clean | Ask |


### credit <a name='sets-credit'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| BI_TDB20224 | Bank of Italy table 20224 contains data on loan origination, excluding bad loans, by region and sector in Italy | 14 | Monthly | 2011 | updated with 3 months lag | Clean | Ask |


### electricity <a name='sets-electricity'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| EIA_923 | EIA form 923 contains monthly data on power generation in US, including net generation, fuel receipts and retail sales by state. | 14 | Monthly | 2001 | up-to-date | Some missing values | Ask |
| EIA_930 | EIA form 930 contains operational data of the american electricity grid including demand, demand forecast and generation by balancing authority. | 14 | Hourly | 2019 | up-to-date | Some missing values | Download parquet from PUDL |


### energy <a name='sets-energy'></a>

| Dataset Name | Short Description | IRP | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| EIA_923 | EIA form 923 contains monthly data on power generation in US, including net generation, fuel receipts and retail sales by state. | 14 | Monthly | 2001 | up-to-date | Some missing values | Ask |


## Datasets by IRP <a name='datasets-by-irp'></a>


### IRP 14 <a name='sets-14'></a>

| Dataset Name | Short Description | Subject(s) | Frequency | First Date | Last Date | Clean | Availability |
|---|---|---|---|---|---|---|---|
| BI_TDB20224 | Bank of Italy table 20224 contains data on loan origination, excluding bad loans, by region and sector in Italy | credit;banking | Monthly | 2011 | updated with 3 months lag | Clean | Ask |
| EIA_923 | EIA form 923 contains monthly data on power generation in US, including net generation, fuel receipts and retail sales by state. | electricity;energy | Monthly | 2001 | up-to-date | Some missing values | Ask |
| EIA_930 | EIA form 930 contains operational data of the american electricity grid including demand, demand forecast and generation by balancing authority. | electricity | Hourly | 2019 | up-to-date | Some missing values | Download parquet from PUDL |
<!-- END INVENTORY -->