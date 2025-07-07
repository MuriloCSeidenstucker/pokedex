from pytest_mock import MockerFixture

# from src.main.process_handle import start


def test_start(mocker: MockerFixture):
    mocker.patch("src.main.process_handle.introduction_process")

    # start()
