Wholesale Shop Management Web Application
Project Overview
    This project is a comprehensive data-driven web application developed using Python and Streamlit to manage operations of a wholesale business. The goal is to digitize and streamline key business functions such as inventory tracking, supplier management, sales monitoring, and visual reporting.
    The system aims to replace manual records with a centralized digital interface that supports real-time interaction with data, efficient reporting, and insightful analytics—all without relying on complex databases.

Objectives
    1. To build a modular and user-friendly interface for managing wholesale business activities.
    2. To implement inventory control, sales tracking, and supplier coordination using simple data structures.
    3. To empower users with data visualization tools for drawing insights from business operations.
    4. To use image processing techniques for managing product visuals and enhancing product-related assets.

Application Scope
This project is designed for:
    1. Retail/Wholesale business owners seeking to digitize their operations.
    2. Inventory managers who need to track stock levels, reorder thresholds, and product categorization.
    3. Sales analysts looking for revenue breakdowns, best-selling products, and trend visualization.
    4. Marketing teams interested in brand-level performance and visual content enhancements.
    5. Educational/demo purposes for learners to understand how to integrate data science and web development.

Technologies Used
    1. Python 3.12 – Core programming language.
    2. Streamlit – Web interface framework for building interactive dashboards with minimal code.
    3. Pandas – Primary library for handling tabular data and filtering operations.
    4. NumPy – Supplementary library for numerical calculations.
    5. Matplotlib – Used for drawing bar graphs, histograms, pie charts, and line plots.
    6. Seaborn – Visualization library for heatmaps and boxplots.
    7. Pillow (PIL) – Image processing library for enhancements and transformations.

CSV Files – Used as data stores simulating lightweight database tables.
Functional Modules
1. Homepage and Navigation
    Custom navigation system using page buttons.
    No sidebar clutter; intuitive layout for easy transitions between pages.
2. Login and Authentication
    Verifies users from a CSV-based login database.
    Ensures restricted access to administrative modules.
3. Add Product
    Input form to add new product details.
    Appends data to products_expanded_updated.csv.
4. Inventory
    Filters based on Brand, Category, or Product ID.
    Displays key product details: price, stock, reorder level, tax rate.
    Highlights low-stock items for proactive inventory management.

5. Supplier Management
    View, add, and filter suppliers by city or brand.
    Data entry form saves to suppliers_updated.csv.

6. Sales Reporting
    Analysis of uploaded sales data (sales_updated.csv).
    Calculates total revenue, quantity sold, top products, and brands.

7. Image Editor
    Uploads images in JPG, PNG, or JPEG format.
    Offers operations like resize, rotate, transpose, sharpen, blur, and enhance.
    Displays original and modified images side-by-side.

8. Reports & Visualizations
Uploads any CSV dataset for visual analysis.
Supports:
    Bar charts
    Line plots
    Pie charts
    Scatter plots
    Histograms
    Box plots
    Heatmaps
Allows custom selection of axes and chart type with error handling.
Data and Storage (Simulated Database)
All data is stored and managed in the form of structured CSV files located in the data/ directory.

Files Used:
1. products_expanded_updated.csv – Product master file.
2. sales_updated.csv – Sales transaction records.
3. suppliers_updated.csv – Supplier contact details.
4. users_updated.csv – User login credentials.
These files are dynamically read and updated using pandas. In a production system, these can be replaced with a relational database (e.g., SQLite, PostgreSQL).

Methods and Implementation Strategy
1. Data Loading – pandas.read_csv() used across modules for loading structured data.
2. Filtering Logic – Applied conditionally based on form inputs using DataFrame masks.
3. Visualization Pipeline – matplotlib and seaborn used to plot graphs with clear labeling.
4. Image Processing – Pillow library used to apply filters and transformations, allowing pre- and post-processing previews.
5. Navigation – st.switch_page() and buttons used for page transitions without clutter.

Potential Enhancements
1. Integration with a relational database (PostgreSQL or MySQL).
2. Role-based access control (Admin vs. Staff).
3. Export reports in PDF or Excel format.
4. Real-time data syncing and dashboard auto-refresh.
5. Mobile-responsive layout using external CSS or Streamlit themes.