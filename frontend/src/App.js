import { HashRouter, Route, Routes } from "react-router-dom";
import Page404 from "./Pages/404";
import Home from "./Pages/Home";

function App() {
  return (
    <div className="App">
      <HashRouter>
        <Routes>
          <Route path="/" exact element={<Home />} />
          <Route path="*" element={<Page404 />} />
        </Routes>
      </HashRouter>
    </div>
  );
}

export default App;
