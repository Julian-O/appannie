#Supported Endpoints - Cross Reference.

### About 

App Annie's documentation describes their API. 

The documentation is a little inconsistent:

* Some parts of the API are listed in an index page, some are not.
* Some parts of the API have separate pages for each API section, some are
lumped together.

This Python API has a related but different structure to the documentation.

This document maps from the API sections described in the documentation to the
methods described in Python API.

Notes:

* The API could be described by folder and filename, or the exact Python call
required. However, here it is described by the name of the class, and the name 
of the method.

* For each operation, the URL is provided to uniquely identify
each endpoint. This doesn't include the parameters. However, it should be
enough to confirm the documentation and the method are talking about equivalent
operations.

# Free APIs

### MetaData API

| Document | Method | EndPoint |
| -------- | ------ | -------- |
| Country | `MetaData.countries()` | `/v1.2/meta/countries` |
| Category | `StoreMetaData.categories()` | `/v1.2/meta/{vertical}/{market}/categories` |
| Category V1.3 | *Unsupported*| `/v1.3/meta/featured_apps/categories`
| Market | `MetaData.markets()` `MetaData.verticals()`  `StoreMetaData.all()`| `/v1.2/meta/markets`
| Currency | `MetaData.currencies()` | `/v1.2/meta/currencies`
| Device | `StoreMetaData.devices()` | `/v1.2/meta/apps/{market}/devices`
| Feed | `StoreMetaData.feeds()` | `/v1.2/meta/apps/{market}/feeds`
| Trans. code → production |  *Unsupported*| `/v1.2/{vertical}/{market}/package-codes2ids`

### Connect API

| Document | Method | EndPoint |
| -------- | ------ | -------- |
| Account Connections | `Account.all()` `Account.page()` | `/v1.2/accounts`
| Account Connection Product | `Product.all()` `Product.page()` | `/v1.2/accounts/{account_id}/products`
| IAP (In Product Purchase) | `Product.iaps()` | `/v1.2/accounts/{account_id}/products/{product_id}/iaps`
| Shared Products | `Account.sharings()` | `/v1.2/sharing/products`
| Product Sales | `Product.sales()` | `/v1.2/accounts/{account_id}/products/{product_id}/sales`
| Account Connection Sales | `Account.sales()` | `/v1.2/accounts/{account_id}/sales`
| Advertising Account Site & Campaign | `Account.ads()` | `/v1.2/accounts/{account_id}/ad_items`
| App Site and Campaign | `App.ads()` | `/v1.2/{vertical}/{market}/{asset}/{product_id}/ad_items` |
| User Advertising | `Account.ad_sales()` | `/v1.2/{vertical}/sales`
| Product Usage | `Product.usage()` | `/v1.2/accounts/{account_id}/products/{product_id}/{data_source}/usage`
| Product Store Metrics | `Product.metrics()` | `/v1.2/accounts/{account_id}/products/{product_id}/store_metrics`

###  Intelligence (Free) API

| Document | Method | EndPoint |
| -------- | ------ | -------- |
| App Details | `App.details()`| `/v1.2/{vertical}/{market}/{asset}/{product_id}/details` |
| App Rank History | `App.ranks()`| `/v1.2/{vertical}/{market}/{asset}/{product_id}/ranks`| 
| App Reviews | `App.reviews()` | `/v1.2/{vertical}/{market}/{asset}/{product_id}/reviews` |
| App Ratings | `App.ratings()` | `/v1.2/{vertical}/{market}/{asset}/{product_id}/ratings` | 
| App Featured: Placement Categories | `FeatureMetaData.categories()` | `/v1.2/meta/feature/categories` |
| App Featured: Placement Types | `FeatureMetaData.types()` | `/v1.2/meta/feature/types` |
| App Featured: Placement Daily Features | `App.featured()`| `/v1.2/{vertical}/{market}/{asset}/{product_id}/featured` |
| App Featured: Placement Feature History | `App.featured_history()`| `/v1.2/{vertical}/{market}/{asset}/{product_id}/featured_history`|

# Premium APIs
### SDK Insights API


| Document | Method | EndPoint |
| -------- | ------ | -------- |
| Top SDKs | *Unsupported* | `/v1.3/intelligence/sdk/top_sdks` |
| SDK Metrics | *Unsupported* | `/v1.3/intelligence/sdk/sdk_metrics` |
| SDK Details | *Unsupported* | `/v1.3/intelligence/sdk/{sdk_id}/details/` |
| SDK Apps | *Unsupported* | `/v1.3/intelligence/sdk/{sdk_id}/apps` |
| App SDKs | *Unsupported* | `/v1.3/intelligence/apps/{app_id}/sdks` |
| Company Level SDKs | *Unsupported* | `/v1.3/intelligence/company/{company_id}/sdks/` |

### Downloads & Revenue Data API

| Document | Method | EndPoint |
| -------- | ------ | -------- |
| Top Apps | `Intelligence.app_ranking()` |`/v1.2/intelligence/{vertical}/{market}/ranking` |
| App History | `Intelligence.app_history()`| `/v1.2/intelligence/{vertical}/{market}/app/{product_id}/history` |
| Top Publishers | *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/publisher-ranking` |
| Publisher History | *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/publisher/{publisher_id}/history` |

### App Store Optimization (ASO) APIs

| Document | Method | EndPoint |
| -------- | ------ | -------- |
| Keyword Explorer | `KeyWord.explore()` | `/v1.2/{vertical}/{market}/keywords/explorer` |
| Product Ranked Keywords | `KeyWord.ranked()` | `/v1.2/{vertical}/{market}/{asset}/{product_id}/keywords/ranked` |
| Product Keyword Performance | `KeyWord.performance`| `/v1.2/{vertical}/{market}/app/{product_id}/keywords/ranks`
| Keyword Management: List/Add/Delete | *Unsupported* | `/v1.2/user/keywords/list`, `/v1.2/user/keywords/add`, `/v1.2/user/keywords/delete`

### Company & Publisher Details APIs
| Document | Method | EndPoint |
| -------- | ------ | -------- |
| Company Details| *Unsupported* | `/v1.2/{org_level}/{company_id}/{detail_type}`|
| Publisher Details | *Unsupported*  | `/v1.2/{org_level}/{market}/{publisher_id}/{detail_type}` |

### DNA Delta API

| Document | Method | EndPoint |
| -------- | ------ | -------- |
| DNA Delta | *Unsupported* | `/v1.3/dna_change/{entity_type}`

### Market Size API

| Document | Method | EndPoint |
| -------- | ------ | -------- |
| Market Size |  *Unsupported* | `/v1.3/intelligence/apps/{market}/market_size` |

### Usage & Engagement Data API

| Document | Method | EndPoint |
| -------- | ------ | -------- |
| Top Apps| *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/usage-ranking` |
| App History| *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/app/{app_id}/usage-history` | 
| User Retention| *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/app/{product_id}/user-retention` |

### Cross-App Usage and Demographics Data API
| Document | Method | EndPoint |
| -------- | ------ | -------- |
| Cross-App Usage | *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/app/{product_id}/cross_app_usage` | 
| App Demographics | *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/app/{product_id}/demographics` |

### User Acquisition (Advertising) Data API
| Document | Method | EndPoint |
| -------- | ------ | -------- |
| Creatives | *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/creatives`|
| Advertisers | *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/advertisers`|
| Ad Monetization | *Unsupported* | `/v1.2/intelligence/apps/ios/advertisers`|
| Ad Platforms | *Unsupported* | `/v1.2/intelligence/apps/ios/advertisers`|
| Advertiser App (Overview) | *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/app/{product_id}/advertiser`|
| Advertiser App (Seen In) | *Unsupported* | `/v1.2/intelligence/{vertical}/{market}/app/{product_id}/advertiser_seen_in`|

###  iOS 11 Featured Apps (Today, Apps and Games) API
| Document | Method | EndPoint |
| -------- | ------ | -------- |
|iOS 11 Featured Apps | *Unsupported* | `/v1.3/{vertical}/{market}/featured_apps` 

### App Store Rankings Top Charts API
| Document | Method | EndPoint |
| -------- | ------ | -------- |
| App Store Rankings Top Charts | *Unsupported* | `/v1.2/{vertical}/{market}/ranking` |


# Partnership APIs
Platform Partnership 
-------------
 *Unsupported* 
 

 
