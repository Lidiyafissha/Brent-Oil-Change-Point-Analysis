const Filters = ({ onChange }) => (
  <div>
    <input type="date" onChange={e => onChange("start", e.target.value)} />
    <input type="date" onChange={e => onChange("end", e.target.value)} />
  </div>
);

export default Filters;
