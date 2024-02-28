import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import LoginSignup from "./pages/LoginSignup.jsx";
import NotFoundPage from "./pages/NotFoundPage.jsx";
import Form from "./pages/Form.jsx";
import UserProfile from "./pages/UserProfile.jsx";

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
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <RouterProvider router={router}></RouterProvider>
);
