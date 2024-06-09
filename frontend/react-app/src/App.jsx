import Layout from "./components/Layout";
import Main from "./components/DynamicList";
import SearchBar from "./components/SearchBar";
import useRedirectToLogin from "./components/RedirectToLogin";

function App() {
  useRedirectToLogin();

  return (
    <Layout>
      <SearchBar />
      <Main />
    </Layout>
  );
}

export default App;
