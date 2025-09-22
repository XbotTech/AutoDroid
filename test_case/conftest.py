import pytest

from common.send_message_url import SendReportMessage
from py_page.base_page import BasePage
import time
from common.log import Logger

logger = Logger().get_logger()


@pytest.fixture
def get_driver():
    driver = BasePage().driver
    yield driver
    driver.quit()


def pytest_terminal_summary(terminalreporter):
    # pytest_terminal_summary函数是pytest的一个插件钩子函数，用于在所有的测试运行完成后向终端报告总结信息
    # 即：收集自动化测试结果，然后统一发送到报告中
    duration = time.time() - terminalreporter._sessionstarttime
    duration = round(duration, 2)

    test_result = dict(
        total=terminalreporter._numcollected,
        deselected=len(terminalreporter.stats.get('deselected', [])),
        passed=len(terminalreporter.stats.get('passed', [])),
        failed=len(terminalreporter.stats.get('failed', [])),
        error=len(terminalreporter.stats.get('error', [])),
        skipped=len(terminalreporter.stats.get('skipped', [])),
        total_time=f"{duration}秒"
    )

    report_str = f'《安卓自动化测试报告》\n' \
                 f'用例执行数: {test_result.get("total")} 条\n' \
                 f'反选的用例: {test_result.get("deselected")} 条\n' \
                 f'通过的用例: {test_result.get("passed")} 条\n' \
                 f'失败的用例: {test_result.get("failed")} 条\n' \
                 f'异常的用例: {test_result.get("error")} 条\n' \
                 f'跳过的用例: {test_result.get("skipped")} 条\n' \
                 f'运行总耗时: {test_result.get("total_time")}'

    logger.info(report_str)

    # 机器人发送自动化测试报告
    SendReportMessage.send_talk_message(report_str)

# 执行测试
# if __name__ == "__main__":
#     ...
# # 创建模拟的terminalreporter
# terminalreporter = mock_terminalreporter()
#
# # 执行测试报告生成
# pytest_terminal_summary(terminalreporter)
