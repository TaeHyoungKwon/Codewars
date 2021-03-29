import time
import unittest


def stat(strng):
    if not strng:
        return ''
    records_list = _parse_records(strng)
    range_ = max(records_list) - min(records_list)
    average = sum(records_list) // len(records_list)
    median = _get_median(records_list)
    return f"Range: {_get_formatted(range_)} Average: {_get_formatted(average)} Median: {_get_formatted(median)}"


def _parse_records(origin_string):
    result = []
    for record in origin_string.split(", "):
        hours, minutes, seconds = map(int, record.split("|"))
        result.append(hours * 3600 + minutes * 60 + seconds)
    return result


def _get_formatted(value):
    return time.strftime("%H|%M|%S", time.gmtime(value))


def _get_median(records):
    sorted_records = sorted(records)
    if len(sorted_records) % 2:
        median = sorted_records[len(sorted_records) // 2]
    else:
        center = len(sorted_records) // 2
        prev_center = center - 1
        median = (sorted_records[center] + sorted_records[prev_center]) // 2
    return median


class TestStat(unittest.TestCase):
    def test_stat_case_with_records_length_is_odd(self):
        self.assertEqual(
            stat(strng="01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"),
            "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34",
        )

    def test_stat_case_with_records_length_is_odd_case_2(self):
        self.assertEqual(
            stat(strng="02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"),
            "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00",
        )

    def test_stat_case_with_records_length_is_even(self):
        self.assertEqual(
            stat(strng="02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|32|34, 2|17|17"),
            "Range: 00|31|17 Average: 02|27|10 Median: 02|24|57",
        )
