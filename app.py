import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout='wide')

st.sidebar.title("User Input")
user_name = st.sidebar.text_input("Enter Your Name")

uploaded_files = st.sidebar.file_uploader(
    "Upload your files (CSV or Excel):", 
    type=["csv", "xlsx"], 
    accept_multiple_files=True
)

if user_name:
    st.sidebar.success(f"Welcome, {user_name}!")

st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")

if uploaded_files:
    st.subheader(f"Uploaded Files by {user_name}")

    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read file with better handling
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(BytesIO(file.getvalue()), engine="openpyxl")  # Improved Handling
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        if df.empty:
            st.warning(f"{file.name} is empty! Please upload a valid file.")
            continue

        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")

        st.write("Preview:")
        st.dataframe(df, height=300)

        st.subheader(f"Data Cleaning for {file.name}")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed ✅")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values Filled ✅")

        st.subheader(f"Select Columns for {file.name}")

        if not df.columns.empty:
            selected_columns = st.multiselect(
                f"Choose Columns", df.columns.tolist(), default=df.columns.tolist()
            )
            df = df[selected_columns]
        else:
            st.warning(f"The uploaded file {file.name} has no columns or is empty.")

        st.subheader(f"Visualization for {file.name}")
        if st.checkbox(f"Show Bar Chart for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

        st.subheader(f"Convert {file.name}")
        conversion_type = st.radio(
            f"Convert {file.name} to:", ["CSV", "Excel"], key=f"{file.name}_{user_name}"
        )

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False, engine='openpyxl')
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("All files have been processed successfully! 🚀")