import {
  LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, ReferenceLine
} from "recharts";

const PriceChart = ({ data, events, changePoints }) => (
  <ResponsiveContainer width="100%" height={400}>
    <LineChart data={data}>
      <XAxis dataKey="Date" />
      <YAxis />
      <Tooltip />

      <Line
        type="monotone"
        dataKey="Price"
        stroke="#1f77b4"
        dot={false}
      />

      {changePoints.map((cp, idx) => (
        <ReferenceLine
          key={idx}
          x={cp.date}
          stroke="red"
          strokeDasharray="3 3"
        />
      ))}

      {events.map((ev, idx) => (
        <ReferenceLine
          key={idx}
          x={ev.Date}
          stroke="orange"
          strokeDasharray="1 1"
        />
      ))}
    </LineChart>
  </ResponsiveContainer>
);

export default PriceChart;
