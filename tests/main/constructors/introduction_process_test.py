from pytest_mock import MockerFixture

from src.main.constructors.introduction_process import introduction_process


def test_introduction_process(mocker: MockerFixture):
    spy = mocker.patch(
        "src.main.constructors.introduction_process.introduction_page",
        side_effect="1",
    )

    result = introduction_process()

    spy.assert_called_once()
    assert isinstance(result, str)
    assert result == "1"
