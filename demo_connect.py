import streamlit as st
from streamlit_flow import streamlit_flow
from streamlit_flow.interfaces import StreamlitFlowEdge, StreamlitFlowNode
import json


# Function to load data from JSON file
def load_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data


def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


data_filepath = "db.json"
data = load_data(data_filepath)

# Format nodes and edges as per the streamlit_flow requirements
nodes = [StreamlitFlowNode(**node) for node in data["nodes"]]
edges = [StreamlitFlowEdge(**edge) for edge in data["edges"]]

element = streamlit_flow(
    # nodes=[
    #     StreamlitFlowNode(
    #         id="1",
    #         data={'label': 'Node 1'},
    #         pos=(100, 100),
    #         type='input',
    #         source_position='right',
    #         target_position='left'
    #     ),
    #     StreamlitFlowNode(
    #         id="2",
    #         data={'label': 'Node 2'},
    #         pos=(100, 110),
    #         type='output',
    #         source_position='right',
    #         target_position='left'
    #     ),
    #     StreamlitFlowNode(
    #         id="3",
    #         data={'label': 'Node 03'},
    #         pos=(100, 120),
    #         type='output',
    #         source_position='right',
    #         target_position='left'
    #     ),
    #     StreamlitFlowNode(
    #         id="4",
    #         data={'label': 'Node 04'},
    #         pos=(100, 130),
    #         type='output',
    #         source_position='right',
    #         target_position='left'
    #     )
    # ],
    # edges=[
    #     StreamlitFlowEdge(
    #         id='1-2',
    #         source='1',
    #         target='2',
    #         animated=True
    #     ),
    #     StreamlitFlowEdge(
    #         id='1-3',
    #         source='1',
    #         target='3',
    #         animated=True
    #     )
    # ],
    nodes=nodes,
    edges=edges,
    direction='right',
    fit_view=True,
    get_node_on_click=True,
    get_edge_on_click=True,
    get_edge_on_connect=True,
)

# if element:
#   st.write(f"Clicked on {element['elementType']} {element['id']}")

if element and 'elementType' in element and element['elementType'] in ['node', 'edge']:
    st.write(f"Clicked on {element['elementType']} {element['id']}")

if element and 'elementType' in element and element['elementType'] in ['edge_connect']:
    st.write(f"Clicked on {element['elementType']}, Source: {element['source']}, Target: {element['target']}")
    # Add new edge to the data
    new_edge = {
        "id": f"{element['source']}-{element['target']}",
        "source": element['source'],
        "target": element['target'],
        "animated": True  # Assuming you want animated edges by default
    }
    data['edges'].append(new_edge)

    # Save the updated data back to db.json
    save_data(data_filepath, data)
