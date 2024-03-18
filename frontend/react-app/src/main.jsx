import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom"

import "./index.css"
import App from "./App.jsx"
import NotFoundPage from "./pages/NotFoundPage.jsx"
import UserProfile from "./pages/UserProfile.jsx"
import RegisterPage from "./pages/RegisterPage.jsx"
import LoginPage from "./components/LoginPage.jsx"

const token = localStorage.getItem("appToken")

const router = createBrowserRouter([
  {
    path: "/",
    element: token ? <App /> : <LoginPage />,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/profile",
    element: <UserProfile></UserProfile>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/register",
    element: <RegisterPage></RegisterPage>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/login",
    element: <LoginPage></LoginPage>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
])

ReactDOM.createRoot(document.getElementById("root")).render(<RouterProvider router={router}></RouterProvider>)