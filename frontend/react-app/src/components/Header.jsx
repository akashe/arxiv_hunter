import { useAuth0 } from "@auth0/auth0-react";
import LoginButton from "./LoginButton";
import LogoutButton from "./LogoutButton";
import { Link } from "react-router-dom";

function Header() {
    const { user, isAuthenticated, isLoading } = useAuth0();
  return (
    <header className="fixed top-0 left-0 right-0 z-10 text-slate-800 h-16 bg-white shadow-md flex items-center justify-between px-6">
      <h1 className="text-2xl font-bold">Arxiv Hunter</h1>
      <div className="hidden lg:block flex-grow"></div>
      <Link
        to={"/profile"}
        className="text-xl font-bold text-slate-800 border-slate-800 text-center bg-slate-200 rounded-full h-10 w-10 hover:bg-slate-300 flex justify-center items-center">
        <img
          src={user.picture}
          className="rounded-full"></img>
      </Link>
      {isAuthenticated ? (
        <LogoutButton></LogoutButton>
      ) : (
        <LoginButton></LoginButton>
      )}
    </header>
  );
}

export default Header;
