**Twitter Stream API** is a Stream Analytics solution for collection of Twitter data via Stream API exposed by Twitter using **Python** Module i.e. Tweepy.

The following describe **high level requirements** for this application:
* **Consumes** Twitter Stream for a specified amount of time
* **Collection** of tweets in form of
    * Raw Data File
    * Cleaned Data File
    * Aggregated Mentions as per configuration
* **Refine** data collected from Stream with lookup capability for given attributes e.g. users, mentions, hashtags etc.
* **Log** all exceptions and failures for analysis

Read the [methodology page](https://github.com/hamzahafeez7/twitter-stream-api/wiki/Methodology-&-Releases) for **step-by-step phases of development** along with their **estimated timeline** and **future goals**

Feel free to provide your feedback on the project. 

Thanks for visiting this repository.

### Pre-requisites & Constraints
Following are the pre-requisites required to run the application
* Twitter applcation created using Twitter development portal
* Credentials to access Twitter application with Read/Write Permissions
* Python 3.8+ Installed

Currently, the application has only been tested with Winodws.
