import { useEffect, useState } from "react";
import {
  fetchPrices,
  fetchEvents,
  fetchChangePoints
} from "../api/api";

import PriceChart from "../components/Pricechart";
import Filters from "../components/filters";

const Dashboard = () => {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  const [filters, setFilters] = useState({});

  useEffect(() => {
    fetchPrices(filters).then(res => setPrices(res.data));
    fetchEvents().then(res => setEvents(res.data));
    fetchChangePoints().then(res => setChangePoints(res.data));
  }, [filters]);

  const updateFilter = (key, value) => {
    setFilters(prev => ({ ...prev, [key]: value }));
  };

  return (
    <>
      <Filters onChange={updateFilter} />
      <PriceChart
        data={prices}
        events={events}
        changePoints={changePoints}
      />
    </>
  );
};

export default Dashboard;
