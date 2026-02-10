const KPICards = ({ volatility, avgChange }) => (
  <div style={{ display: "flex", gap: "1rem" }}>
    <div>Volatility: {volatility}</div>
    <div>Avg Price Change: {avgChange}%</div>
  </div>
);

export default KPICards;
