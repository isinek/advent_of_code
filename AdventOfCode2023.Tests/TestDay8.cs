using AdventOfCode2023.Solvers;

namespace Tests
{
    public class TestDay8
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
			string[] test_input = {
				"RL",
				"",
				"AAA = (BBB, CCC)",
				"BBB = (DDD, EEE)",
				"CCC = (ZZZ, GGG)",
				"DDD = (DDD, DDD)",
				"EEE = (EEE, EEE)",
				"GGG = (GGG, GGG)",
				"ZZZ = (ZZZ, ZZZ)"
			};
			SolverDay8 solver = new SolverDay8();

			Assert.That(solver.Part1(test_input), Is.EqualTo(2));
        }

        [Test]
        public void Test2()
        {
			string[] test_input = {
				"LLR",
				"",
				"AAA = (BBB, BBB)",
				"BBB = (AAA, ZZZ)",
				"ZZZ = (ZZZ, ZZZ)"
			};
			SolverDay8 solver = new SolverDay8();

			Assert.That(solver.Part1(test_input), Is.EqualTo(6));
        }

        [Test]
        public void Test3()
        {
			string[] test_input = {
				"LR",
				"",
				"11A = (11B, XXX)",
				"11B = (XXX, 11Z)",
				"11Z = (11B, XXX)",
				"22A = (22B, XXX)",
				"22B = (22C, 22C)",
				"22C = (22Z, 22Z)",
				"22Z = (22B, 22B)",
				"XXX = (XXX, XXX)"
			};
			SolverDay8 solver = new SolverDay8();

			Assert.That(solver.Part2(test_input), Is.EqualTo(6));
        }
    }
}
