import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const useRedirectToLogin = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const appToken = localStorage.getItem("appToken");
    if (!appToken) {
      navigate("/login");
    }
  }, [navigate]);
};

export default useRedirectToLogin;