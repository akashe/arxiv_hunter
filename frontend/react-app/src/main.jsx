import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom"
import { ToastContainer } from "react-toastify"
import "react-toastify/dist/ReactToastify.css"

import App from "./App.jsx"
import NotFoundPage from "./ui/NotFoundPage.jsx"
import UserProfile from "./user/UserProfile.jsx"
import RegisterPage from "./auth/RegisterPage.jsx"
import LoginPage from "./auth/LoginPage.jsx"
import Test from "./Test.jsx"
import "./index.css"

const token = localStorage.getItem("appToken")

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
    element: token ? <UserProfile loggedIn={token ? true : false}></UserProfile> : <LoginPage />,
    errorElement: <NotFoundPage />,
  },
  {
    path: "/register",
    element: <RegisterPage />,
    errorElement: <NotFoundPage />,
  },
  {
    path: "/test",
    element: <Test />,
    errorElement: <NotFoundPage />,
  },
])

ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <RouterProvider router={router} />
    <ToastContainer />
  </>
)