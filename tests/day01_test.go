package days

import (
	"testing"

	"github.com/go-jose/go-jose/v4/testutils/assert"
	"github.com/isinek/aoc/days"
)

func TestDailRotation(t *testing.T) {
	tcs := map[string]struct {
		startPosition    int
		left             bool
		steps            int
		expectedPosition int
		expectedZeros    uint64
	}{
		"Left rotation": {
			startPosition:    50,
			left:             true,
			steps:            10,
			expectedPosition: 40,
			expectedZeros:    0,
		},
		"Right rotation": {
			startPosition:    50,
			left:             false,
			steps:            10,
			expectedPosition: 60,
			expectedZeros:    0,
		},
		"Left rotation - 2 full circles, and more": {
			startPosition:    50,
			left:             true,
			steps:            210,
			expectedPosition: 40,
			expectedZeros:    2,
		},
		"Right rotation - 2 full circles, and more": {
			startPosition:    50,
			left:             false,
			steps:            210,
			expectedPosition: 60,
			expectedZeros:    2,
		},
		"Left rotation - to zero": {
			startPosition:    50,
			left:             true,
			steps:            50,
			expectedPosition: 0,
			expectedZeros:    1,
		},
		"Right rotation - to zero": {
			startPosition:    50,
			left:             false,
			steps:            50,
			expectedPosition: 0,
			expectedZeros:    1,
		},
		"Left rotation - to zero after 2 circles": {
			startPosition:    50,
			left:             true,
			steps:            250,
			expectedPosition: 0,
			expectedZeros:    3,
		},
		"Right rotation - to zero after 2 circles": {
			startPosition:    50,
			left:             false,
			steps:            250,
			expectedPosition: 0,
			expectedZeros:    3,
		},
		"Right 1000 rotation": {
			startPosition:    50,
			left:             false,
			steps:            1000,
			expectedPosition: 50,
			expectedZeros:    10,
		},
		"Left rotation - from 0, 2 circles": {
			startPosition:    0,
			left:             true,
			steps:            200,
			expectedPosition: 0,
			expectedZeros:    2,
		},
		"Right rotation - from 0, 2 circles": {
			startPosition:    0,
			left:             false,
			steps:            200,
			expectedPosition: 0,
			expectedZeros:    2,
		},
	}
	for name, tc := range tcs {
		t.Run(name, func(t *testing.T) {
			dail, zeros := days.DailRotation(tc.startPosition, tc.left, tc.steps)

			assert.Equal(t, dail, tc.expectedPosition)
			assert.Equal(t, zeros, tc.expectedZeros)
		})
	}
}

func TestExample1(t *testing.T) {
	result, err := days.SolutionDay1Task1("./day01_example.in")
	assert.NoError(t, err)
	assert.Equal(t, result, uint64(3))
}

func TestExample2(t *testing.T) {
	result, err := days.SolutionDay1Task2("./day01_example.in")
	assert.NoError(t, err)
	assert.Equal(t, result, uint64(6))
}
