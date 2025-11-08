import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Excel Data Merger & Dashboard", layout="wide")

st.title("📊 Excel Data Merger & Dashboard")

# Upload multiple Excel files
uploaded_files = st.file_uploader(
    "📂 Upload one or more Excel files",
    type=["xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    dfs = []
    for file in uploaded_files:
        df = pd.read_excel(file)
        dfs.append(df)
        st.write(f"✅ Loaded: {file.name} ({df.shape[0]} rows, {df.shape[1]} cols)")

    st.success(f"Uploaded {len(uploaded_files)} files successfully!")

    # Merge logic
    merge_option = st.radio("How would you like to merge these files?",
                            ["Concatenate (stack all rows)", "Merge on a specific column"])

    if merge_option == "Concatenate (stack all rows)":
        merged_df = pd.concat(dfs, ignore_index=True)
    else:
        common_cols = set.intersection(*(set(df.columns) for df in dfs))
        merge_col = st.selectbox("Select common column to merge on:", list(common_cols))
        merged_df = dfs[0]
        for df in dfs[1:]:
            merged_df = pd.merge(merged_df, df, on=merge_col, how="outer")

    st.write(f"🧾 Combined DataFrame shape: {merged_df.shape}")
    st.dataframe(merged_df.head(10))

    # --- FILTERING ---
    with st.expander("🔍 Filter Data"):
        all_cols = merged_df.columns.tolist()
        filter_col = st.selectbox("Select column to filter:", all_cols)
        unique_vals = merged_df[filter_col].dropna().unique().tolist()
        selected_vals = st.multiselect("Choose filter values:", unique_vals)
        if selected_vals:
            merged_df = merged_df[merged_df[filter_col].isin(selected_vals)]
            st.write(f"Filtered rows: {merged_df.shape[0]}")

    # --- PIVOT TABLE ---
    with st.expander("📈 Pivot Table & Charts"):
        all_cols = merged_df.columns.tolist()
        index_col = st.selectbox("Rows (index):", all_cols, key="index")
        values_col = st.selectbox("Values (to summarize):", all_cols, key="values")
        aggfunc = st.selectbox("Aggregation:", ["sum", "mean", "count", "max", "min"])
        if st.button("Generate Pivot Table"):
            pivot_df = pd.pivot_table(
                merged_df,
                index=index_col,
                values=values_col,
                aggfunc=aggfunc
            ).reset_index()
            st.subheader("📊 Pivot Table Result")
            st.dataframe(pivot_df)

            fig = px.bar(pivot_df, x=index_col, y=values_col,
                         title=f"{aggfunc.title()} of {values_col} by {index_col}")
            st.plotly_chart(fig, use_container_width=True)

    # --- SUMMARY STATISTICS ---
    with st.expander("📋 Summary Statistics"):
        st.write(merged_df.describe(include='all').T)

    # --- DOWNLOAD MERGED DATA ---
    st.download_button(
        label="⬇️ Download merged dataset (CSV)",
        data=merged_df.to_csv(index=False).encode('utf-8'),
        file_name="merged_data.csv",
        mime="text/csv"
    )
