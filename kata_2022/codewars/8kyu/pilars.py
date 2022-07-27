# def pillars(num_pill, dist, width):
#     return (num_pill - 1) * (dist * 100) + ((num_pill - 2) * width) if num_pill != 1 else 0

def pillars(num_pill, dist, width):
    return (num_pill - 1) * (dist * 100) + max((num_pill - 2), 0) * width


class TestPillars:
    def test_pillars(self):
        assert pillars(1, 10, 10) == 0
        assert pillars(2, 20, 25) == 2000
        assert pillars(11, 15, 30) == 15270
