/*
< Code Writing Idea Flow >

Plan (Try 1):
	1. Make Three parts:
		Data part,
		Structure part,
		Main part

		1.1. Data part
			Which type should I use for saving data
			slice? or struct? or map?

		1.2. Struct part
			Make Two structs?
				Make Device struct and inherit it to Electrics struct like a python class?

		1.3. Main part
			I Think if 1.1 and 1.2 are made well, it will be easy.
			Just calculate and print it.

Plan (Try 2):
	2. I decided to make Struct part first and then make Data using Struct.

Consequence:
	3. I made Struct that abstracts ElectricDevice.
		3.1. I made fields
		3.2. But I failed to make methods that calculate daily, monthly, yearly power consumption. So I made methods outside of Struct.
		3.3. If the function (e T) is defined outside of Struct, it looks like callable by T.method()

	4. I made data slice of ElectricDevice in Data part.
	5. I Calculated total daily, monthly, yearly power consumption in Main part.
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
	return e.dailyPowerConsumption() * 365
}

// Data part ===========================================================================================================
var electricDevices = []ElectricDevice{
	{name: "PLED", power: 20, cnt: 4, dailyUsageTime: 12},
	{name: "Philips", power: 16, cnt: 4, dailyUsageTime: 12},
	{name: "FarmTec", power: 12, cnt: 1, dailyUsageTime: 12},
	{name: "LED_BAR", power: 7.2, cnt: 10, dailyUsageTime: 12},
	{name: "Synology_NAS", power: 25, cnt: 1, dailyUsageTime: 24},
}

// Main part ===========================================================================================================
func main() {

	var (
		totalDailyPowerConsumption   float64
		totalMonthlyPowerConsumption float64
		totalYearlyPowerConsumption  float64
	)

	for _, v := range electricDevices {
		totalDailyPowerConsumption += v.dailyPowerConsumption()
		totalMonthlyPowerConsumption += v.monthlyPowerConsumption()
		totalYearlyPowerConsumption += v.yearlyPowerConsumption()
	}

	fmt.Println()
	fmt.Printf("Total Daily Power Consumption: %.3f kWh\n", totalDailyPowerConsumption)
	fmt.Printf("Total Monthly Power Consumption: %.3f kWh\n", totalMonthlyPowerConsumption)
	fmt.Printf("Total Yearly Power Consumption: %.3f kWh\n", totalYearlyPowerConsumption)
}
