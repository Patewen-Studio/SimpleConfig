from unittest import TestCase, main
from simpleconfig import SimpleConfig


PATH_TO_TEST_CONFIG = './test.smpl'


class TestConfig(TestCase):
    def test_config(self):
        config = SimpleConfig()
        config.parse(PATH_TO_TEST_CONFIG)
        self.assertEqual(
            "1", config.get("key")
        )
        print(config.int("key"))


if __name__ == '__main__':
    main()
