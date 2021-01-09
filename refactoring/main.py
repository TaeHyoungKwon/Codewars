import json
import math


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f"청구 내역 (고객명: {invoice['customer']})\n"
    dollar_format = '${:,.2f}'

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        this_amount = 0

        if play["type"] == "tragedy":
            this_amount = 40000
            if perf["audience"] > 30:
                this_amount += 1000 * (perf["audience"] - 30)
        elif play["type"] == "comedy":
            this_amount = 30000
            if perf["audience"] > 20:
                this_amount += 10000 + 500 * (perf["audience"] - 20)
            this_amount += 300 * perf["audience"]
        else:
            raise Exception("알 수 없는 장르")

        volume_credits += max(perf["audience"] - 30, 0)

        if play["type"] == "comedy":
            volume_credits += math.floor(perf["audience"] / 5)

        result += f' {play["name"]}: {dollar_format.format(this_amount / 100)} ({perf["audience"]}석)\n'
        total_amount += this_amount

    result += f"총액: {dollar_format.format(total_amount / 100)}\n"
    result += f"적립 포인트': {volume_credits}점\n"
    return result


if __name__ == '__main__':
    with open('invoices.json') as json_file:
        invoice = json.load(json_file)[0]

    with open('plays.json') as json_file:
        plays = json.load(json_file)

    print(statement(invoice, plays))


