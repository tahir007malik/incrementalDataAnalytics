# incrementalDataAnalytics
This project demonstrates incremental analysis of car sales data. The project leverages a medallion architecture to efficiently process and analyze sales data over time, enabling stakeholders to gain insights into sales trends, customer preferences, and inventory management.

## Directory Structure

The `/Data` folder contains the source files:
- **IncrementalSales.csv**: Contains the incremental sales data.
- **SalesData.csv**: Contains the historical sales data.

---

## Pipeline Workflow

### 1. **Data Ingestion**
- **Source**: CSV files (`IncrementalSales.csv` and `SalesData.csv`) located in the `/Data` folder on GitHub.
- **Tool**: Azure Data Factory (ADF).
- **Process**: ADF ingests data from GitHub and stores it in an **Azure SQL Database**.

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

---

## Technologies Used
- **Azure Data Factory**: For data ingestion and the orchestration of the entire pipeline.
- **Azure SQL Database**: Intermediate storage for ingested data.
- **Azure Data Lake Storage Gen2 (ADLS Gen2)**: For hierarchical data storage across bronze, silver, and gold layers.
- **Azure Databricks**: For data transformation and schema creation.
- **Power BI/Tableau**: For visualization and business intelligence.

---

## Star Schema Design
- **Fact Table**:
  - `factsales`: Contains measures such as sales amount, quantity, and keys linking to dimension tables.
- **Dimension Tables**:
  - `dim_branch`: Details about branches.
  - `dim_date`: Date-related attributes.
  - `dim_dealer`: Dealer information.
  - `dim_model`: Model details.

---

## Project Files
- **/Data**: Contains the initial CSV files.
- **Azure Data Factory Pipeline**: Used for data ingestion and orchestration.
- **Databricks Notebooks**: Used for silver layer transformations and gold layer schema creation.
- **Parquet Files**: Stored in ADLS Gen2 across bronze, silver, and gold layers.

---

## Future Enhancements
- Automate the incremental data ingestion process using ADF triggers.
- Implement CI/CD for pipeline deployment.
- Add real-time data processing using Kafka or Event Hubs.
- Expand visualization capabilities with additional KPIs and dashboards.

---

## Usage Instructions
1. Clone the repository and locate the `/Data` folder.
2. Set up Azure resources (ADF, Azure SQL Database, ADLS Gen2, and Databricks).
3. Configure pipelines in Azure Data Factory for data ingestion and orchestration.
4. Use Databricks notebooks to process and transform data.
5. Visualize the processed data using Power BI or Tableau.

---

This documentation provides a comprehensive overview of the `Incremental Data Analytics` project, ensuring ease of understanding and reproducibility for collaborators and viewers.
