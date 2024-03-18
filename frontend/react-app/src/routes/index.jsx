import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { useAuth } from "../provider/authProvider";
import { ProtectedRoute } from "./ProtectedRoute"
import Logout from "../pages/Logout"
import Register from "../pages/RegisterPage"
import LoginPage from "../components/LoginPage"
import App from "../App"

const Routes = () => {
  const { token } = useAuth()

  // Define public routes accessible to all users
  const routesForPublic = [
    {
      path: "/register",
      element: <Register></Register>,
    },
    {
      path: "/login",
      element: <LoginPage></LoginPage>,
    },
  ]

  // Define routes accessible only to authenticated users
  const routesForAuthenticatedOnly = [
    {
      path: "/",
      element: <ProtectedRoute />, // Wrap the component in ProtectedRoute
      children: [
        {
          path: "/",
          element: <App></App>,
        },
        {
          path: "/profile",
          element: <div>User Profile</div>,
        },
        {
          path: "/logout",
          element: <Logout />,
        },
      ],
    },
  ]

  // Define routes accessible only to non-authenticated users
  const routesForNotAuthenticatedOnly = [
    {
      path: "/",
      element: <div>Home Page</div>,
    },
    {
      path: "/login",
      element: <LoginPage />,
    },
  ]

  // Combine and conditionally include routes based on authentication status
  const router = createBrowserRouter([...routesForPublic, ...(!token ? routesForNotAuthenticatedOnly : []), ...routesForAuthenticatedOnly])

  // Provide the router configuration using RouterProvider
  return <RouterProvider router={router} />
}

export default Routes;
