"""Hello world pytest for app.py testing."""

from unittest.mock import Mock, patch
import app


def test_hello_world():
    """Hello world test to verify pytest is working."""
    assert True


def test_main():
    """Test the main function runs without errors."""
    with (
        patch("app.init_database") as mock_init,
        patch("app.st.error") as mock_error,
        patch("app.st.success") as mock_success,
        patch("app.st.columns") as mock_columns,
        patch("app.st.subheader"),
        patch("app.st.text_area"),
        patch("app.st.button"),
        patch("app.st.markdown"),
        patch("app.st.write"),
        patch("app.st.dataframe"),
        patch("app.st.info"),
        patch("app.st.warning"),
    ):
        # Mock successful database connection
        mock_conn = Mock()
        mock_conn.execute.return_value.get_as_df.return_value.empty = True
        mock_init.return_value = (Mock(), mock_conn)

        # Mock columns as context managers
        mock_col1 = Mock()
        mock_col2 = Mock()
        mock_col1.__enter__ = Mock(return_value=mock_col1)
        mock_col1.__exit__ = Mock(return_value=None)
        mock_col2.__enter__ = Mock(return_value=mock_col2)
        mock_col2.__exit__ = Mock(return_value=None)
        mock_columns.return_value = [mock_col1, mock_col2]

        # Run main function
        app.main()

        # Verify database initialization was called
        mock_init.assert_called_once()
        mock_success.assert_called_once()
        mock_error.assert_not_called()


def test_main_database_failure():
    """Test main function handles database connection failure."""
    with patch("app.init_database") as mock_init, patch("app.st.error") as mock_error:
        # Mock failed database connection
        mock_init.return_value = (None, None)

        # Run main function
        app.main()

        # Verify error handling
        mock_init.assert_called_once()
        mock_error.assert_called_once_with("❌ Unable to connect to the database")
