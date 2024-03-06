import useAuth0 from "@auth0/auth0-react";

const Auth0Login = () => {
  const { loginWithRedirect, isAuthenticated } = useAuth0();
  return (
    !isAuthenticated && (
      <button onClick={() => loginWithRedirect()}>SignIn</button>
    )
  );
};

export default Auth0Login;
