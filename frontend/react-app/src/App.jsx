import Header from "./components/Header";
import Main from "./components/DynamicList";
import SearchBar from "./components/SearchBar";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [token, setToken] = useState(null);

  const handleLoginSuccess = (token) => {
    // Store token in localStorage (or other secure storage)
    localStorage.setItem("token", token);
    setIsLoggedIn(true);
    setToken(token);
    // Optionally, redirect to a specific page after login (e.g., home page)
    // navigate('/home');
  };
  return (
    <div className="max-w-[800px] min-w-min bg-white mx-auto m-0">
      <Header></Header>
      <SearchBar></SearchBar>
      <Main></Main>
    </div>
  );
}

export default App;
