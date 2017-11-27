#!/bin/bash
python structuredatabase.py &
wait
python populatedatabase.py &
wait
python clean_database.py &
wait
python distance_database.py
wait
python plot_distance.py
wait
python plot_emissions.py
wait
python plot_cost.py
wait
python plot_emissions_leaf.py
wait
python plot_cost_leaf.py
wait
python plot_emission_savings.py
wait
python plot_cost_savings.py
