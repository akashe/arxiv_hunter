import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import LoginSignup from "./pages/LoginSignup.jsx";
import NotFoundPage from "./pages/NotFoundPage.jsx";
import Form from "./pages/Form.jsx";
import UserProfile from "./pages/UserProfile.jsx";
import Register from "./components/Register.jsx";
import TestRegister from "./components/TestRegister.jsx";
import Login from "./components/Login.jsx";
import DashBoard from "./dashboard/DashBoard.jsx";
import { ToastContainer } from "react-toastify";
import "react-toastify/ReactToastify.min.css";
import { Auth0Provider } from "@auth0/auth0-react";

const domain = import.meta.env.REACT_APP_AUTH0_DOMAIN;
const clientId = import.meta.env.REACT_APP_AUTH0_CLIENT_ID;

const router = createBrowserRouter([
  {
    path: "/",
    element: <App></App>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/auth",
    element: <LoginSignup></LoginSignup>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/form",
    element: <Form></Form>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/profile",
    element: <UserProfile></UserProfile>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/register",
    element: <Register></Register>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/testregister",
    element: <TestRegister></TestRegister>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/login",
    element: <Login></Login>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/dashboard",
    element: <DashBoard></DashBoard>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <Auth0Provider
    domain={domain}
    clientId={clientId}
    redirectUri={window.location.origin}>
    <ToastContainer />
    <RouterProvider router={router}></RouterProvider>
  </Auth0Provider>
);
