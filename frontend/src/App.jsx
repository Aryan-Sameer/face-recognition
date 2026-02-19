import { RouterProvider, createBrowserRouter } from 'react-router-dom'

import Home from "./pages/Home";
import Assistant from "./pages/Assistant";
import Sidebar from "./components/Sidebar";
import Navigation from "./pages/Navigation";

function App() {

  const router = createBrowserRouter([
    {
      path: "/",
      element: <><Home /> <Sidebar /></>
    },
    {
      path: "/assistant",
      element: <><Assistant /> <Sidebar /></>
    },
    {
      path: "/navigation",
      element: <><Navigation /> <Sidebar /></>
    },
  ])

  return (
    <div className="flex h-screen font-mono">
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
