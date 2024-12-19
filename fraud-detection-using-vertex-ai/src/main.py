def main():
    from src.data.loader import load_data
    from src.data.preprocessing import preprocess_data
    from src.model.trainer import train_model
    from src.model.evaluator import evaluate_model
    from src.model.deployer import deploy_model # type: ignore

    # Load Data
    train_data, test_data = load_data()

    # Preprocess Data
    processed_train, processed_test = preprocess_data(train_data, test_data)

    # Train Model
    model, metrics = train_model(processed_train, processed_test)

    # Evaluate Model
    evaluate_model(model, metrics)

    # Deploy Model
    deploy_model(model)

if __name__ == "__main__":
    main()