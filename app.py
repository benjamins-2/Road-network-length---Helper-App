import streamlit as st
import osmnx as ox

place = st.text_input(
    "Input the city name here, (example 'Vratsa, Vratsa Bulgaria')",
    placeholder="Vratsa, Vratsa Bulgaria",
    value="Vratsa, Vratsa Bulgaria",
)


def get_graph(place):
    G = ox.graph_from_place(place, network_type="drive")
    G = ox.convert.to_undirected(G)
    return G


def get_fig(G):
    fig, _ = ox.plot_graph(ox.project_graph(G), show=False)
    return fig


def plot_graph(G):
    fig = get_fig(G)
    st.pyplot(fig)


def compute_road_network_length(G):
    edge_length = ox.stats.street_length_total(G)
    return edge_length


with st.spinner("Computing network length"):
    G = get_graph(place)
    edge_length = compute_road_network_length(G)
    edge_length_km = round(edge_length / 1000)
    st.write(f"Road Network length is {edge_length_km} km")
with st.spinner("Computing graph to display"):
    plot_graph(G)
