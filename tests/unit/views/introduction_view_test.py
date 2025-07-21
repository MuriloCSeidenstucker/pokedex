from pytest_mock import MockerFixture

from src.views.introduction_view import introduction_page


def test_introduction_page(mocker: MockerFixture):
    mock_add_column = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_column", side_effect=mock_add_column)
    mock_add_row = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_row", side_effect=mock_add_row)
    mock_panel_fit = mocker.patch("rich.panel.Panel.fit")
    mock_print = mocker.patch("rich.console.Console.print")
    mock_input = mocker.patch("rich.console.Console.input", return_value="foo")

    response = introduction_page()

    mock_panel_fit.assert_called_once()
    mock_print.assert_called_once()
    mock_input.assert_called_once()
    assert mock_add_column.call_count == 2
    assert mock_add_row.call_count == 6
    assert response == "foo"
