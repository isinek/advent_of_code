using AdventOfCode2023.Solvers;

namespace Tests
{
    public class TestDay1
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
			string[] test_input = {
				"1abc2",
				"pqr3stu8vwx",
				"a1b2c3d4e5f",
				"treb7uchet"
			};
			SolverDay1 solver = new SolverDay1();

			Assert.That(solver.Part1(test_input), Is.EqualTo(142));
		}

        [Test]
        public void Test2()
        {
			string[] test_input = {
				"two1nine",
				"eightwothree",
				"abcone2threexyz",
				"xtwone3four",
				"4nineeightseven2",
				"zoneight234",
				"7pqrstsixteen"
			};
			SolverDay1 solver = new SolverDay1();

			Assert.That(solver.Part2(test_input), Is.EqualTo(281));
		}
	}
}
