/*
Experiment 1:
	1. Result:
		1.1 Syntax
			func (e Struct) funcName() returnDataType {
				// func body
				return returnData
			}
		1.2 This function is able to call by struct variable

*/

package main

import "fmt"

// Struct part =========================================================================================================

// ElectricDevice Struct for electric device
type ElectricDevice struct {
	name           string
	power          float64 // unit: watt
	cnt            int     // unit: ea
	dailyUsageTime int     // unit: hour

}

// dailyPowerConsumption unit: kWh
func (e ElectricDevice) dailyPowerConsumption() float64 {
	return e.power * float64(e.cnt) * float64(e.dailyUsageTime) / 1000
}

// monthlyPowerConsumption unit: kWh
func (e ElectricDevice) monthlyPowerConsumption() float64 {
	return e.dailyPowerConsumption() * 30
}

// yearlyPowerConsumption unit: kWh
func (e ElectricDevice) yearlyPowerConsumption() float64 {
	return e.monthlyPowerConsumption() * 12
}

// Main part ===========================================================================================================
func main() {

	var experimentDevice = ElectricDevice{
		name:           "ExperimentDevice",
		power:          10,
		cnt:            1,
		dailyUsageTime: 24,
	}

	fmt.Println("Call by method of ElectricDevice")
	fmt.Println("Actually, in Golang it was just structure variable")

	fmt.Println("dailyPowerConsumption: ", experimentDevice.dailyPowerConsumption())

}
