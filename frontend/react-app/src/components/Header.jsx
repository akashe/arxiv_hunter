import { Link, useLocation } from "react-router-dom";

function Header() {
  const location = useLocation();
  const isTodayPage = location.pathname === "/today";

  return (
    <header className="fixed top-0 left-0 right-0 z-10 text-slate-800 h-16 bg-white shadow-md flex items-center justify-between px-6">
      <Link to="/" className="text-2xl font-bold">
        Arxiv Hunter
      </Link>
      <div className="flex-grow flex justify-center">
        <Link
          to={isTodayPage ? "/" : "/today"}
          className="text-lg font-semibold text-center px-4 py-2 rounded-md hover:bg-gray-200"
        >
          {isTodayPage ? "Your Feed" : "Today's Papers"}
        </Link>
      </div>
      <Link
        to="/profile"
        className="text-xl font-bold text-center bg-lime-100 rounded-full h-10 w-10 hover:bg-orange-200 flex justify-center items-center"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="black"
          className="w-6 h-6"
        >
          <path
            fillRule="evenodd"
            d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z"
            clipRule="evenodd"
          />
        </svg>
      </Link>
    </header>
  );
}

export default Header;
