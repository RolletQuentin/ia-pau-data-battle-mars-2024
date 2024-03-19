import { HashRouter, Route, Routes } from "react-router-dom";
import Page404 from "./Pages/404";
import Home from "./Pages/Home";
import CustomScrollbar from "./Components/test";

function App() {
  return (
    <div className="App">
      <HashRouter>
        <Routes>
          <Route path="/" exact element={<Home />} />
          <Route path="/test" element={<CustomScrollbar />} />
          <Route path="*" element={<Page404 />} />
        </Routes>
      </HashRouter>
    </div>
  );
}

export default App;
