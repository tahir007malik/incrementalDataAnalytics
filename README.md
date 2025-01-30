# incrementalDataAnalytics
This project demonstrates incremental analysis of car sales data. It leverages a medallion architecture to efficiently process and analyze sales data over time, enabling stakeholders to gain insights into sales trends, customer preferences, and inventory management.

## Video Documentation
Link: [YouTube](https://youtu.be/adW2WUgc55s)

## Directory Structure

The `/Data` folder contains the source files:
- **IncrementalSales.csv**: Contains the incremental sales data.
- **SalesData.csv**: Contains the historical sales data.

The `/Docs` folder contains:
- **incrementalDataAnalyticsThumbnail.png**: Project thumbnail
- **incrementalDataAnalyticsWorkflow.png**: Explains project workflow

The `/Notebooks` folder contains:
- `/DimensionTables`: contains notebooks for all dimension tables

    - `goldDimBranchNotebook.ipynb`: pyspark notebook for creating branch dimension table
    - `goldDimDateNotebook.ipynb`: pyspark notebook for creating date dimension table
    - `goldDimDealerNotebook.ipynb`: pyspark notebook for creating dealer dimension table
    - `goldDimModelNotebook.ipynb`: pyspark notebook for creating model dimension table

- `/FactTables`: contains notebooks for all fact table
    
    - `goldFactTableNotebook.ipynb`: pyspark notebook for creating carsales fact table
- `/SilverLayer`: contains notebooks for silver layer transformation

The `/SQL` folder contains:

- `1. sourceCarsData.sql`: for creating **source_cars_data** table 
- `2. waterTable.sql`: for creating **water_table** table 
- `3. updateWatermarkTable.sql`: for creating stored procedure **updateWatermarkTable**

## Pipeline Workflow
![Pipeline Workflow](https://github.com/tahir007malik/incrementalDataAnalytics/blob/main/Docs/incrementalDataAnalyticsWorkflow.png)

### 1. **Data Ingestion**
- **Source**: CSV files (`IncrementalSales.csv` and `SalesData.csv`) located in the `/Data` folder on GitHub.
- **Tool**: Azure Data Factory (ADF).
- **Process**: ADF ingests data from GitHub and stores it inside a database named `carsales` on **Azure SQL Database**.

### 2. **Bronze Layer (Raw Data)**
- **Storage**: Azure Data Lake Storage Gen2 (ADLS Gen2).
- **Format**: Parquet.
- **Process**: Raw data from Azure SQL Database is stored in the bronze layer of ADLS Gen2 for archival and further processing.

### 3. **Silver Layer (Transformed Data)**
- **Tool**: Azure Databricks.
- **Notebook**: A Databricks notebook is used for data cleaning, transformation, and enrichment.
- **Storage**: Transformed data is stored in the silver layer of ADLS Gen2.

### 4. **Gold Layer (Analytics-Ready Data)**
- **Tool**: Azure Databricks.
- **Catalog**: Databricks catalog named `cars_catalog` is created.
- **Schema**: Inside the catalog, a schema named `gold` is created.
- **Tables**: Using the Star Schema design, the following tables are created:
  - `dim_branch`
  - `dim_date`
  - `dim_dealer`
  - `dim_model`
  - `factsales`
- **Storage**: Analytics-ready data is stored in the gold layer of ADLS Gen2.

### 5. **Visualization**
- **Tools**: Power BI and Tableau.
- **Purpose**: The data from the gold layer is used for creating dashboards and visualizations to derive business insights.

## Technologies Used
- **Azure Data Factory**: For data ingestion and the orchestration of the entire pipeline.
- **Azure SQL Database**: Intermediate storage for ingested data.
- **Azure Data Lake Storage Gen2 (ADLS Gen2)**: For hierarchical data storage across bronze, silver, and gold layers.
- **Azure Databricks**: For data transformation and schema creation.
- **Power BI/Tableau**: For visualization and business intelligence.

## Star Schema Design
- **Fact Table**:
  - `factsales`: Contains measures such as revenue, units_sold, rev_per_unit, and keys (dim_model_key, dim_branch_key, dim_dealer_key, dim_date_key) linking to dimension tables.
- **Dimension Tables**:
  - `dim_branch`: Details about branches.
  - `dim_date`: Date-related attributes.
  - `dim_dealer`: Dealer information.
  - `dim_model`: Model details.

## Azure Data Factory Pipeline
![Star Schema used inside pipeline](https://github.com/tahir007malik/incrementalDataAnalytics/blob/main/Docs/incrementalDataAnalyticsPipeline.png)

## Project Files
- **/Data**: Contains the initial CSV files.
- **/Notebooks**: Contains pyspark notebooks for data transformation.
- **/SQL**: Contains SQL files for creating tables, stored-procedures **Azure SQL Database**.
- **Azure Data Factory Pipeline**: Used for data ingestion and orchestration.
- **Databricks Notebooks**: Used for silver layer transformations and gold layer schema creation.
- **Parquet Files**: Stored in ADLS Gen2 across bronze, silver, and gold layers.

## Future Enhancements
- Automating the incremental data ingestion process using ADF triggers.
- Adding real-time data processing using Kafka or Event Hubs.
- Expanding visualization capabilities with additional KPIs and dashboards.

## Usage Instructions
1. Clone the repository and locate the `/Data` folder.
2. Set up Azure resources (ADF, Azure SQL Database, ADLS Gen2, and Databricks).
3. Configure pipelines in Azure Data Factory for data ingestion and orchestration.
4. Use Databricks notebooks to process and transform data.
5. Visualize the processed data using Power BI or Tableau.

This documentation provides a comprehensive overview of the `Incremental Data Analytics` project, ensuring ease of understanding and reproducibility for collaborators and viewers.
