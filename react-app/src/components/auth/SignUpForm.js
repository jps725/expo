import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import { TextField, Button, Grid, Link, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  form: {
    width: "100%",
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
  paper: {
    margin: theme.spacing(8, 4),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
}));

const SignUpForm = () => {
  const classes = useStyles();
  const [restaurantName, setRestaurantName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(restaurantName, email, password));
      if (data.errors) {
        setErrors(data.errors);
      }
    }
  };

  const updateRestaurantName = (e) => {
    setRestaurantName(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className={classes.paper}>
      <Typography component="h1" variant="h5">
        Sign Up
      </Typography>
      <form className={classes.form} onSubmit={onSignUp}>
        <div>
          {errors.map((error) => (
            <div> {error} </div>
          ))}
        </div>

        <TextField
          variant="outlined"
          margin="normal"
          required
          fullWidth
          id="restaurantName"
          label="Restaurant Name"
          name="restaurantName"
          autoFocus
          onChange={updateRestaurantName}
          value={restaurantName}
        />
        <TextField
          variant="outlined"
          margin="normal"
          required
          fullWidth
          id="email"
          label="Email"
          name="email"
          autoComplete="email"
          autoFocus
          onChange={updateEmail}
          value={email}
        />
        <TextField
          variant="outlined"
          margin="normal"
          required
          fullWidth
          type="password"
          label="Password"
          name="password"
          id="password"
          onChange={updatePassword}
          value={password}
        />
        <TextField
          variant="outlined"
          margin="normal"
          required
          fullWidth
          type="password"
          label="Repeat Password"
          name="repeatPassword"
          id="repeatPassword"
          onChange={updateRepeatPassword}
          value={repeatPassword}
        />
        <Button
          type="submit"
          fullWidth
          variant="contained"
          color="primary"
          className={classes.submit}
        >
          Sign Up
        </Button>

        <Grid container>
          <Grid item xs>
            <Link href="/" variant="body2">
              {"Already have an account? Sign In"}
            </Link>
          </Grid>
        </Grid>
      </form>
    </div>
  );
};

export default SignUpForm;
