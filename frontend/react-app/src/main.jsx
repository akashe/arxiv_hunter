import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import App from "./App.jsx";
import TodaysPaper from './components/TodaysPaper.jsx';
import NotFoundPage from "./ui/NotFoundPage.jsx";
import UserProfile from "./user/UserProfile.jsx";
import RegisterPage from "./auth/RegisterPage.jsx";
import LoginPage from "./auth/LoginPage.jsx";
import Test from "./Test.jsx";
import Layout from "./components/Layout";
import "./index.css";

const token = localStorage.getItem("token");

const router = createBrowserRouter([
  {
    path: "/",
    element: token ? <App /> : <LoginPage />,
    errorElement: <NotFoundPage />,
  },
  {
    path: "/login",
    element: <LoginPage />,
    errorElement: <NotFoundPage />,
  },
  {
    path: "/profile",
    element: token ? (
      <Layout>
        <UserProfile loggedIn={!!token} />
      </Layout>
    ) : (
      <LoginPage />
    ),
    errorElement: <NotFoundPage />,
  },
  {
    path: "/register",
    element: <RegisterPage />,
    errorElement: <NotFoundPage />,
  },
  {
    path: "/test",
    element: (
      <Layout>
        <Test />
      </Layout>
    ),
    errorElement: <NotFoundPage />,
  },
  {
    path: "/today",
    element: token ? (
      <Layout>
        <TodaysPaper />
      </Layout>
    ) : (
      <LoginPage />
    ),
    errorElement: <NotFoundPage />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <RouterProvider router={router} />
    <ToastContainer />
  </>
);
