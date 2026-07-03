import matplotlib.pyplot as plt


def plot_churn_by_region(churn_region):

    plt.figure()
    churn_region.plot(kind="bar", color="indianred")
    plt.title("Churn Rate by Region (%)")
    plt.xlabel("Region")
    plt.ylabel("Churn Rate (%)")
    plt.tight_layout()
    plt.savefig("outputs/churn_by_region.png")
    plt.show()


def plot_churn_by_segment(churn_segment):

    plt.figure()
    churn_segment.plot(kind="bar", color="darkorange")
    plt.title("Churn Rate by Value Segment (%)")
    plt.xlabel("Segment")
    plt.ylabel("Churn Rate (%)")
    plt.tight_layout()
    plt.savefig("outputs/churn_by_segment.png")
    plt.show()


def plot_segment_distribution(segment_dist):

    plt.figure()
    segment_dist.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Customer Value Segment Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("outputs/segment_distribution.png")
    plt.show()


def plot_spend_by_region(region_spend):

    plt.figure()
    region_spend.plot(kind="bar", color="steelblue")
    plt.title("Total Spend by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Spend")
    plt.tight_layout()
    plt.savefig("outputs/spend_by_region.png")
    plt.show()
