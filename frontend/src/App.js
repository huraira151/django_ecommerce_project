import './App.css';
import { Routes, Route } from "react-router-dom";
import { connect } from 'react-redux';
// import RouteGuard from './RouterGuard';
// import AuthLayout from './layout/Auth/index';
// import Admin from './layout/Admin';
// import { history } from './reduxStore/store';
import LoginScreen from './pages/AuthScreens/Login';
import SignUpScreen from './pages/AuthScreens/SignUp';
import Home from './pages/Home';

function App() {
  // const { loginInfo } = props;

  return (
    <div className="App">
      <Routes>
        <Route path='login' element={<LoginScreen />} />
        <Route path='signup' element={<SignUpScreen />} />
        <Route path='/' element={<Home />} />
      </Routes>
    </div>
  );
}

const mapStateToProps = (state) => ({
  loginInfo: state.login.loginInfo,
});

export default connect(mapStateToProps, null)(App);
