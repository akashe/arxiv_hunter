import Header from "./components/Header";
import Main from "./components/DynamicList";
import SearchBar from "./components/SearchBar";
import useRedirectToLogin from "./components/RedirectToLogin";

function App() {
  useRedirectToLogin();
  return (
    <div className="max-w-[800px] min-w-min bg-white mx-auto m-0">
      <Header></Header>
      <SearchBar></SearchBar>
      <Main></Main>
    </div>
  );
}

export default App;