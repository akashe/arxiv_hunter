import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom"

import App from "./App.jsx"
import NotFoundPage from "./ui/NotFoundPage.jsx"
import UserProfile from "./user/UserProfile.jsx"
import RegisterPage from "./auth/RegisterPage.jsx"
import LoginPage from "./auth/LoginPage.jsx"
import "./index.css"

const token = localStorage.getItem("appToken")

const router = createBrowserRouter([
  {
    path: "/",
    element: token ? <App /> : <LoginPage />,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/login",
    element: <LoginPage></LoginPage>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/profile",
    element: <UserProfile loggedIn={token ? true : false}></UserProfile>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/register",
    element: <RegisterPage></RegisterPage>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
])

ReactDOM.createRoot(document.getElementById("root")).render(<RouterProvider router={router}></RouterProvider>)