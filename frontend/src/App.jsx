import { useEffect, useState } from "react";

function App() {
  const [market, setMarket] = useState({ volatility: "--" });
  const [risk, setRisk] = useState({
    volatility: "--",
    exposure: "--",
    risk_score: "--",
  });
  const [hedged, setHedged] = useState(null);

  const fetchMarket = async () => {
    const res = await fetch("http://127.0.0.1:5000/market");
    setMarket(await res.json());
  };

  const fetchRisk = async () => {
    const res = await fetch("http://127.0.0.1:5000/risk");
    setRisk(await res.json());
  };

  const hedgePortfolio = async () => {
    const res = await fetch("http://127.0.0.1:5000/hedge");
    setHedged(await res.json());
  };

  useEffect(() => {
    fetchMarket();
    fetchRisk();
  }, []);

  return (
    <div style={{ padding: "40px", fontFamily: "Arial", color: "white" }}>
      <h1>🌋 Volatility Volcano Manager</h1>

      <button onClick={fetchMarket}>🔄 Refresh Market</button>{" "}
      <button onClick={fetchRisk}>📊 Recalculate Risk</button>{" "}
      <button onClick={hedgePortfolio}>🛡 Hedge Portfolio</button>

      <hr />

      <h2>📈 Market</h2>
      <p>Volatility Index: <strong>{market.volatility}</strong></p>

      <h2>⚠️ Risk Metrics</h2>
      <p>Volatility: {risk.volatility}</p>
      <p>Exposure: {risk.exposure}</p>
      <p><strong>Risk Score: {risk.risk_score}</strong></p>

      {hedged && (
        <>
          <h2>🛡 Hedging Result</h2>
          <p>Original Exposure: {hedged.original_exposure}</p>
          <p>Hedged Exposure: {hedged.hedged_exposure}</p>
          <p><strong>New Risk Score: {hedged.risk_score}</strong></p>
        </>
      )}
    </div>
  );
}

export default App;
