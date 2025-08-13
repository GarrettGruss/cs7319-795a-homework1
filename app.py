import streamlit as st
import kuzu

st.set_page_config(
    page_title="Kuzu GraphRAG Frontend",
    page_icon="🔗",
    layout="wide"
)

st.title("🔗 Kuzu GraphRAG Database Frontend")
st.markdown("### Hello World! Welcome to your Kuzu graph database interface.")

@st.cache_resource
def init_database():
    try:
        db = kuzu.Database("./kuzu_db")
        conn = kuzu.Connection(db)
        return db, conn
    except Exception as e:
        st.error(f"Failed to connect to Kuzu database: {e}")
        return None, None

def main():
    db, conn = init_database()
    
    if conn is None:
        st.error("❌ Unable to connect to the database")
        return
    
    st.success("✅ Successfully connected to Kuzu database!")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Database Info")
        try:
            result = conn.execute("SHOW TABLES;")
            tables = result.get_as_df()
            if not tables.empty:
                st.write("Tables in database:")
                st.dataframe(tables)
            else:
                st.info("No tables found in database")
        except Exception as e:
            st.warning(f"Could not retrieve tables: {e}")
    
    with col2:
        st.subheader("🔍 Query Interface")
        query = st.text_area(
            "Enter your Cypher query:",
            value="MATCH (n) RETURN n LIMIT 10;",
            height=100
        )
        
        if st.button("Execute Query"):
            try:
                result = conn.execute(query)
                df = result.get_as_df()
                st.write("Query Results:")
                st.dataframe(df)
            except Exception as e:
                st.error(f"Query error: {e}")
    
    st.markdown("---")
    st.markdown("**Ready to build your GraphRAG application!** 🚀")

if __name__ == "__main__":
    main()