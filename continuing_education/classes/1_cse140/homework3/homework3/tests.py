# CSE 140
# Tests for Homework 3: Election prediction

# You do not have to turn in this file.
# You will modify this file by uncommenting lines at its very end, bit by
# bit as you complete your program.


# The "from election import *" statement loads all the functions defined in
# election.py into the current environment.
from election import *


def test_read_csv():
    # No tests provided for the read_csv function
    pass

    
def test_row_to_edge():
    row1 = { "Dem": 5, "Rep": 90 }
    assert row_to_edge(row1) == -85

    row2 = { "Dem": 57.5, "Rep": 77.5 }
    assert row_to_edge(row2) == -20

    row3 = { "Dem": 52, "Rep": 49, "Lib": 1 }
    assert row_to_edge(row3) == 3


def test_state_edges():
    rows1 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1'}]
    assert state_edges(rows1) == {'WA': 0.9}

    rows2 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1'},
               {'State': 'CA', 'Dem': '0.2', 'Rep': '1.3'}]
    assert state_edges(rows2) == {'WA': 0.9, 'CA': -1.1}


def test_earlier_date():
    assert earlier_date("Jan 01 2012", "Jan 02 2012")
    assert earlier_date("Jan 31 2012", "Feb 1 2012")
    assert not earlier_date("Dec 31 2012", "Jan 01 2012")
    assert earlier_date("Apr 12 2012", "Jun 12 2012")


poll_rows1 = [{"ID":1, "State":"WA", "Pollster":"A", "Date":"Jan 07 2010"},
              {"ID":2, "State":"WA", "Pollster":"B", "Date":"Mar 21 2010"},
              {"ID":3, "State":"WA", "Pollster":"A", "Date":"Jan 08 2010"},
              {"ID":4, "State":"OR", "Pollster":"A", "Date":"Feb 10 2010"},
              {"ID":5, "State":"WA", "Pollster":"B", "Date":"Feb 10 2010"},
              {"ID":6, "State":"WA", "Pollster":"B", "Date":"Mar 22 2010"}]


def test_most_recent_poll_row():
    assert most_recent_poll_row(poll_rows1, "A", "OR") == {"ID":4, "State":"OR", "Pollster":"A", "Date":"Feb 10 2010"}
    assert most_recent_poll_row(poll_rows1, "A", "WA") == {"ID":3, "State":"WA", "Pollster":"A", "Date":"Jan 08 2010"}
    assert most_recent_poll_row(poll_rows1, "B", "WA") == {"ID":6, "State":"WA", "Pollster":"B", "Date":"Mar 22 2010"}
    assert most_recent_poll_row(poll_rows1, "B", "OR") == None
    assert most_recent_poll_row(poll_rows1, "DoesNotExist", "DoesNotExist") == None


def test_unique_column_values():
    assert unique_column_values(poll_rows1, "ID") == { 1, 2, 3, 4, 5, 6 }
    assert unique_column_values(poll_rows1, "State") == { "WA", "OR" }
    assert unique_column_values(poll_rows1, "Pollster") == { "A", "B" }
    assert unique_column_values(poll_rows1, "Date") == { "Jan 07 2010", "Jan 08 2010", "Feb 10 2010", "Mar 21 2010", "Mar 22 2010" }


def test_pollster_predictions():
    rows1 = [{'State': 'WA', 
                'Dem': '1.0', 
                'Rep': '0.1', 
                'Date': 'Nov 04 2008', 
                'Pollster': 'PPP'}]
    assert pollster_predictions(rows1) == {'PPP': {'WA': 0.9}}

    rows2 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]
    assert pollster_predictions(rows2) == {'PPP': {'WA': 0.9, 'CA': -9.3}}

    rows3 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'},
      {'State': 'WA', 'Dem': '9.1', 'Rep': '7.1', 'Date': 'Nov 05 2008', 'Pollster': 'IPSOS'},
      {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'IPSOS'}]
    assert pollster_predictions(rows3) == {'PPP': {'WA': 0.9, 'CA': -1.1}, 
                                             'IPSOS': {'WA': 2.0, 'CA': -9.3}}
                                             
    rows4 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'WA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]
    assert pollster_predictions(rows4) == {'PPP': {'WA': 0.9}}

    rows5 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'},
      {'State': 'OR', 'Dem': '9.1', 'Rep': '7.1', 'Date': 'Nov 05 2008', 'Pollster': 'IPSOS'}]

    assert pollster_predictions(rows5) == {'PPP': {'CA': -1.1, 'WA': 0.9}, 'IPSOS': {'OR': 2.0}}


def test_average_error():
    state_edges_pred_1 = {'WA': 1.0, 'CA': -2.3, 'ID': -20.1}
    state_edges_act_1 = {'WA': 2.1, 'CA': -1.4, 'ID': -19.1}
    assert average_error(state_edges_pred_1, state_edges_act_1) == 1.0

    state_edges_pred_2 = {'WA': 1.0, 'CA': 2.0}
    state_edges_act_2 = {'WA': 2.0, 'CA': 1.0}
    assert average_error(state_edges_pred_2, state_edges_act_2) == 1.0

    state_edges_pred_3 = {'WA': 1.0, 'CA': 2.0}
    state_edges_act_3 = {'WA': 2.0, 'CA': 1.0, 'MA': 2.4, 'OR': -3.9}
    assert average_error(state_edges_pred_3, state_edges_act_3) == 1.0

    state_edges_pred_4 = {'WA': 1.0}
    state_edges_act_4 = {'WA': 0.0}
    assert average_error(state_edges_pred_4, state_edges_act_4) == 1.0


def test_pollster_errors():
    predictions = {
      'PPP': {'WA': 1.0, 'CA': -2.0, 'ID': -20.0}, 
      'ISPOP': {'WA': 2.0, 'ID': -19.0} 
      }
    actual = {'WA': 2.0, 'CA': -1.0, 'ID': -19.0, 'OR': 2.2, 'DC': 0.1}
    assert pollster_errors(predictions, actual) == {'PPP': 1.0, 'ISPOP': 0.0}


def test_pivot_nested_dict():

    us_wars_by_name = {
        "Revolutionary" : { "start": 1775, "end": 1783 },
        "Mexican" : { "start": 1846, "end": 1848 },
        "Civil" : { "start": 1861, "end": 1865 }
        }
    us_wars_by_start_and_end = {
        'start': {'Revolutionary': 1775, 'Civil': 1861, 'Mexican': 1846},
        'end': {'Revolutionary': 1783, 'Civil': 1865, 'Mexican': 1848}
        }
    assert pivot_nested_dict(us_wars_by_name) == us_wars_by_start_and_end

    pnd_input = { "a" : { "x": 1, "y": 2 },
                  "b" : { "x": 3, "z": 4 } }
    pnd_output = {'y': {'a': 2},
                  'x': {'a': 1, 'b': 3},
                  'z': {'b': 4} }
    assert pivot_nested_dict(pnd_input) == pnd_output


def test_average_error_to_weight():
    assert average_error_to_weight(.25) == 16.0
    assert average_error_to_weight(1) == 1.0
    assert average_error_to_weight(2) == 0.25
    assert average_error_to_weight(4) == 0.0625


def test_weighted_average():
    assert weighted_average([3, 4, 5], [1, 1, 1]) == 4
    assert weighted_average([3, 4], [1, 1]) == 3.5
    assert weighted_average([2, 4, 4, 6], [1, 1, 1, 5]) == 5
    assert weighted_average([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]) == 3
    assert weighted_average([1, 2, 1], [3, 2, 5]) == 1.2


def test_pollster_to_weight():
    pollster_errors = {"Gallup":4, "Rasmussen":10, "SurveyUSA":.25}
    assert pollster_to_weight("Gallup", pollster_errors) == 0.0625
    assert pollster_to_weight("SurveyUSA", pollster_errors) == 16
    assert pollster_to_weight("Google", pollster_errors) == 0.04


def test_average_edge():
    assert average_edge({"p1":3, "p2":4, "p3":5}, {"p1":1, "p2":1, "p3":1}) == 4
    assert average_edge({"p1":3, "p2":4, "p3":5}, {"p1":1, "p2":1, "p3":1, "p4":2, "p5": -8}) == 4
    assert average_edge({"p1":3, "p2":4}, {"p1":1, "p2":1}) == 3.5
    assert average_edge({"p1":2, "p2":4, "p3":4, "p4":6}, {"p1":1, "p2":1, "p3":1, "p4":5}) == 3.3684210526315788
    assert average_edge({"p1":1, "p2":2, "p3":3, "p4":4, "p5":5},
                        {"p1":1, "p2":2, "p3":3, "p4":4, "p5":5}) == 1.560068324160182
    assert average_edge({"p1":3, "p2":4, "p3":5}, {"p1":5, "p2":5}) == 4
    assert average_edge({"p1":3, "p2":4, "p3":5}, {}) == 4


def test_predict_state_edges():    
    pollster_predictions = {
      'PPP': { 'WA': -11.2, 'CA': -2.0, 'ID': -1.1 },
      'IPSOS': { 'WA': -8.7, 'CA': -3.1, 'ID': 4.0 },
      'SurveyUSA': { 'WA': -9.0, 'FL': 0.5 },
      }
    pollster_errors = {'PPP': 1.2, 'IPSOS': 4.0, 'SurveyUSA':3.5, 'NonExistant':100.0}
    assert predict_state_edges(pollster_predictions, pollster_errors) == {'CA':
    -2.0908256880733944, 'FL': 0.5, 'ID': -0.6788990825688075, 'WA': -10.799509886766941}


def test_electoral_college_outcome():
    electoral_college = [
      {'State': 'AK', 'Name': 'Alaska', 'Electors': 2, 'Population': 710000},
      {'State': 'AL', 'Name': 'Alabama', 'Electors': 8, 'Population': 4780000},
      {'State': 'AR', 'Name': 'Arkansas', 'Electors': 4, 'Population': 2916000}
    ]
    state_edges = {'AK': -4.0, 'AL': 2.0, 'AR': 1.0}
    assert electoral_college_outcome(electoral_college, state_edges) == {'Rep': 2.0, 'Dem': 12.0}
    
    state_edges = {'AK': -4.0, 'AL': 0.0, 'AR': 1.0}
    assert electoral_college_outcome(electoral_college, state_edges) == {'Rep': 6.0, 'Dem': 8.0}




# If this file, tests.py, is run as a Python script (such as by typing
# "python tests.py" at the command shell), then run the following tests:
if __name__ == "__main__":
    # TODO: Uncomment these function calls as you complete each part, to test
    # your implementation:

    test_read_csv()
    test_row_to_edge()
    #test_state_edges()
    test_earlier_date()
    #test_most_recent_poll_row()
    #test_unique_column_values()
    #test_pollster_predictions()
    #test_average_error()
    #test_pollster_errors()
    #test_pivot_nested_dict()
    #test_weighted_average()
    test_pollster_to_weight()
    test_average_error_to_weight()
    #test_average_edge()
    #test_predict_state_edges()
    test_electoral_college_outcome()

    print "Tests passed."
